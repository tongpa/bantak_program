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

__all__ = ['ExpensesList', 'ExpensesSubList', 'Expenses' ]

class ExpensesList(DeclarativeBase):
    __tablename__ = 'expenses_list';
    expenses_list_id = Column(Integer, autoincrement=True, primary_key=True);
    expenses_list_name = Column(String(255), unique=True, nullable=False);
    
    def __init__(self):
        self.expenses_list_id = None;
        self.expenses_list_name = None;
        
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
        return DBSession.query(cls).filter(  cls.expenses_list_id != '0' ).order_by(cls.expenses_list_id).all();
        
    
class ExpensesSubList(DeclarativeBase):
    __tablename__ = 'expenses_sub_list';
    expenses_sub_list_id = Column(Integer, autoincrement=True, primary_key=True);
    expenses_list_id = Column(   Integer,ForeignKey('expenses_list.expenses_list_id'), nullable=False, index=True) ;
    expenses_list  = relation('ExpensesList', backref='expenses_sub_list');
    expenses_sub_list_name = Column(String(255),  nullable=False);
    expenses_sub_list_other =  Column(String(2),  nullable=False,  default= 0);
    
    def __init__(self):
        self.expenses_sub_list_id = None;
        self.expenses_list_id = 0;         
        self.expenses_sub_list_name = None;
        self.expenses_sub_list_other = '0';
        
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
        return DBSession.query(cls).order_by(cls.expenses_sub_list_id).all();
    @classmethod
    def listByGroup(cls,group):
        return DBSession.query(cls).filter(  cls.expenses_list_id==str(group) ).order_by(cls.expenses_list_id ).all();
    
    
class Expenses(DeclarativeBase):
    __tablename__ = 'expenses';
    expenses_id = Column(Integer, autoincrement=True, primary_key=True);
    expenses_list_id = Column(   Integer,ForeignKey('expenses_list.expenses_list_id'), nullable=False, index=True) ;
    expenses_list  = relation('ExpensesList', backref='expenses');
    expenses_sub_list_id = Column(   Integer,ForeignKey('expenses_sub_list.expenses_sub_list_id'), nullable=False, index=True) ;
    expenses_sub_list  = relation('ExpensesSubList', backref='expenses');
    fiscal_year =   Column(String(4), index=True,  nullable=False);    
    estimate  =   Column(   Integer , nullable=True, default= 0) ;
    detail  = Column(   Text, nullable=True);
    income_other = Column(   Text, nullable=True);
    create_date =  Column(DateTime, nullable=False, default=datetime.now);
    
    def __init__(self):
        self.expenses_id = None;
        self.expenses_list_id = 0;         
        
        self.expenses_sub_list_id = None;
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
            sql = sql + " and expenses_list_id = " + group;
        if(subgroup):
            sql = sql + " and expenses_sub_list_id = " + subgroup;
         
            
        log.info(sql);
        return DBSession.query(cls).filter(sql).all();
    
    @classmethod
    def queryGraphByFiscalYear(cls,year,expenses_list='%'):
        sql = text(""" 
                    select   
                        main.expenses_list_name ,
                        IFNULL(SUM(expenses_year.estimate)    ,0) sum_estimate 
                    from  
                     (   
                          select  
                            expenses_list.expenses_list_id,  
                            expenses_list.expenses_list_name,  
                            expenses_sub_list.expenses_sub_list_id,  
                            expenses_sub_list.expenses_sub_list_name 
                          from   
                            expenses_sub_list inner join expenses_list on expenses_sub_list.expenses_list_id = expenses_list.expenses_list_id  
                        ) as main  
                        left join (  
                          SELECT  
                            expenses.estimate,  
                            expenses.fiscal_year,  
                            expenses.expenses_list_id,  
                            expenses.expenses_sub_list_id   
                          from        
                            expenses   
                          where expenses.fiscal_year=:fiscal_year 
                        ) expenses_year  
                      on ( main.expenses_list_id = expenses_year.expenses_list_id and main.expenses_sub_list_id = expenses_year.expenses_sub_list_id)  
                    where   
                        main.expenses_list_id like :expenses_list_id
                    GROUP BY
                        main.expenses_list_name
                    ORDER BY  
                        main.expenses_list_id,  
                        main.expenses_sub_list_id
                """ , bindparams=[ bindparam('fiscal_year', str(year)), bindparam('expenses_list_id',str(expenses_list))]);
        result = DBSession.execute(sql );
        return result ; 
    @classmethod
    def queryGroupByFiscalYear(cls,year,expenses_list= '%'):
        sql = text("""select   
                main.expenses_list_name,  
                main.expenses_sub_list_name,  
                IFNULL(expenses_year.estimate,0) as estimate,  
                IFNULL(expenses_year.fiscal_year,:show_year ) as fiscal_year,  
                main.expenses_list_id,
                main.expenses_sub_list_id
              from  
                (   
                  select  
                    expenses_list.expenses_list_id,  
                    expenses_list.expenses_list_name,  
                    expenses_sub_list.expenses_sub_list_id,  
                    expenses_sub_list.expenses_sub_list_name 
                  from   
                    expenses_sub_list inner join expenses_list on expenses_sub_list.expenses_list_id = expenses_list.expenses_list_id  
                ) as main  
                left join (  
                  SELECT  
                    expenses.estimate,  
                    expenses.fiscal_year,  
                    expenses.expenses_list_id,  
                    expenses.expenses_sub_list_id   
                  from        
                    expenses   
                  where expenses.fiscal_year=:fiscal_year  
                ) expenses_year  
              on ( main.expenses_list_id = expenses_year.expenses_list_id and main.expenses_sub_list_id = expenses_year.expenses_sub_list_id)  
              where   
                   main.expenses_list_id like :expenses_list_id
              ORDER BY  
                main.expenses_list_id,  
                 main.expenses_sub_list_id """ , bindparams=[bindparam('show_year', str(year)),bindparam('fiscal_year', str(year)), bindparam('expenses_list_id',str(expenses_list))] );
        #log.info(sql);
        result = DBSession.execute(sql );
        return result ; #DBSession.query(cls).filter(sql).all();