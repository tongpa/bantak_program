import os
from datetime import datetime
import sys
try:
    from hashlib import sha1
except ImportError:
    sys.exit('ImportError: No module named hashlib\n'
             'If you are on python2.4 this library is not part of python. '
             'Please install it. Example: easy_install hashlib')

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime, String, Text
from sqlalchemy.orm import relation, synonym
from sqlalchemy import *;
from comcenter.model import DeclarativeBase, metadata, DBSession
#from sqlalchemy.sql.expression import *;
import logging;
import sys;
log = logging.getLogger(__name__);

__all__ = ['RevenueList', 'RevenueSubList', 'Revenue' ]

class RevenueList(DeclarativeBase):
    __tablename__ = 'revenue_list';
    revenue_list_id = Column(Integer, autoincrement=True, primary_key=True);
    revenue_list_name = Column(String(255), unique=True, nullable=False);
    
    def __init__(self):
        self.revenue_list_id = None;
        self.revenue_list_name = None;
        
    def save(self):
        DBSession.add(self); 
        DBSession.flush() ;
    
    def update(self):
        DBSession.update(self);
        
    def remove(self):
        DBSession.delete(self);
        DBSession.flush() ;
    @classmethod
    def getById(cls,id):
        return DBSession.query(cls) .get(id);    
    @classmethod
    def listAll(cls):
        return DBSession.query(cls).filter(  cls.revenue_list_id != '0' ).order_by(cls.revenue_list_id).all();
        
    
class RevenueSubList(DeclarativeBase):
    __tablename__ = 'revenue_sub_list';
    revenue_sub_list_id = Column(Integer, autoincrement=True, primary_key=True);
    revenue_list_id = Column(   Integer,ForeignKey('revenue_list.revenue_list_id'), nullable=False, index=True) ;
    revenue_list  = relation('RevenueList', backref='revenue_sub_list');
    revenue_sub_list_name = Column(String(255),  nullable=False);
    revenue_sub_list_other =  Column(String(2),  nullable=False,  default= 0);
    
    def __init__(self):
        self.revenue_sub_list_id = None;
        self.revenue_list_id = 0;         
        self.revenue_sub_list_name = None;
        self.revenue_sub_list_other = '0';
        
    def save(self):
        DBSession.add(self); 
        DBSession.flush() ;
    
    def update(self):
        DBSession.update(self);
        
    def remove(self):
        DBSession.delete(self);
        DBSession.flush() ;
    @classmethod
    def getById(cls,id):
        return DBSession.query(cls) .get(id);    
    @classmethod
    def listAll(cls):
        return DBSession.query(cls).order_by(cls.revenue_sub_list_id).all();
    @classmethod
    def listByGroup(cls,group):
        return DBSession.query(cls).filter(  cls.revenue_list_id==str(group) ).order_by(cls.revenue_list_id ).all();
    
    
class Revenue(DeclarativeBase):
    __tablename__ = 'revenue';
    revenue_id = Column(Integer, autoincrement=True, primary_key=True);
    revenue_list_id = Column(   Integer,ForeignKey('revenue_list.revenue_list_id'), nullable=False, index=True) ;
    revenue_list  = relation('RevenueList', backref='revenue');
    revenue_sub_list_id = Column(   Integer,ForeignKey('revenue_sub_list.revenue_sub_list_id'), nullable=False, index=True) ;
    revenue_sub_list  = relation('RevenueSubList', backref='revenue');
    fiscal_year =   Column(String(4), index=True,  nullable=False);    
    estimate  =   Column(   Integer , nullable=True, default= 0) ;
    detail  = Column(   Text, nullable=True);
    income_other = Column(   Text, nullable=True);
    create_date =  Column(DateTime, nullable=False, default=datetime.now);
    
    def __init__(self):
        self.revenue_id = None;
        self.revenue_list_id = 0;         
        
        self.revenue_sub_list_id = None;
        self.fiscal_year = None;
        self.estimate = 0;
        self.detail = None;
        self.income_other=  None;
        self.create_date =  datetime.now();
        
    def save(self):
        DBSession.add(self); 
        DBSession.flush() ;
    
    def update(self):
        DBSession.update(self);
        
    def remove(self):
        DBSession.delete(self);
        DBSession.flush() ;
    @classmethod
    def getById(cls,id):
        return DBSession.query(cls) .get(id);    
    @classmethod
    def listAll(cls):
        return DBSession.query(cls).order_by(cls.fiscal_year).all();
    
    @classmethod
    def search(cls,fiscalyear = None, group= None, subgroup= None):
        sql = "1=1 ";
        if (fiscalyear):
            sql = sql + " and fiscal_year = " + fiscalyear;
        if(group):
            sql = sql + " and revenue_list_id = " + group;
        if(subgroup):
            sql = sql + " and revenue_sub_list_id = " + subgroup;
         
            
        log.info(sql);
        return DBSession.query(cls).filter(sql).all();
    
    @classmethod
    def queryGraphByFiscalYear(cls,year,revenue_list='%'):
        sql = text(""" 
                    select   
                        main.revenue_list_name ,
                        IFNULL(SUM(revenue_year.estimate)    ,0) sum_estimate 
                    from  
                     (   
                          select  
                            revenue_list.revenue_list_id,  
                            revenue_list.revenue_list_name,  
                            revenue_sub_list.revenue_sub_list_id,  
                            revenue_sub_list.revenue_sub_list_name 
                          from   
                            revenue_sub_list inner join revenue_list on revenue_sub_list.revenue_list_id = revenue_list.revenue_list_id  
                        ) as main  
                        left join (  
                          SELECT  
                            revenue.estimate,  
                            revenue.fiscal_year,  
                            revenue.revenue_list_id,  
                            revenue.revenue_sub_list_id   
                          from        
                            revenue   
                          where revenue.fiscal_year=:fiscal_year 
                        ) revenue_year  
                      on ( main.revenue_list_id = revenue_year.revenue_list_id and main.revenue_sub_list_id = revenue_year.revenue_sub_list_id)  
                    where   
                        main.revenue_list_id like :revenue_list_id
                    GROUP BY
                        main.revenue_list_name
                    ORDER BY  
                        main.revenue_list_id,  
                        main.revenue_sub_list_id
                """ , bindparams=[ bindparam('fiscal_year', str(year)), bindparam('revenue_list_id',str(revenue_list))]);
        result = DBSession.execute(sql );
        return result ; 
   
    @classmethod
    def queryGroupByFiscalYear(cls,year,revenue_list= '%'):
        sql = text("""select   
                main.revenue_list_name,  
                main.revenue_sub_list_name,  
                IFNULL(revenue_year.estimate,0) as estimate,  
                IFNULL(revenue_year.fiscal_year,:show_year ) as fiscal_year,  
                main.revenue_list_id,
                main.revenue_sub_list_id
              from  
                (   
                  select  
                    revenue_list.revenue_list_id,  
                    revenue_list.revenue_list_name,  
                    revenue_sub_list.revenue_sub_list_id,  
                    revenue_sub_list.revenue_sub_list_name 
                  from   
                    revenue_sub_list inner join revenue_list on revenue_sub_list.revenue_list_id = revenue_list.revenue_list_id  
                ) as main  
                left join (  
                  SELECT  
                    revenue.estimate,  
                    revenue.fiscal_year,  
                    revenue.revenue_list_id,  
                    revenue.revenue_sub_list_id   
                  from        
                    revenue   
                  where revenue.fiscal_year=:fiscal_year  
                ) revenue_year  
              on ( main.revenue_list_id = revenue_year.revenue_list_id and main.revenue_sub_list_id = revenue_year.revenue_sub_list_id)  
              where   
                   main.revenue_list_id like :revenue_list_id
              ORDER BY  
                main.revenue_list_id,  
                 main.revenue_sub_list_id """ , bindparams=[bindparam('show_year', str(year)),bindparam('fiscal_year', str(year)), bindparam('revenue_list_id',str(revenue_list))] );
        #log.info(sql);
        result = DBSession.execute(sql );
        return result ; #DBSession.query(cls).filter(sql).all();