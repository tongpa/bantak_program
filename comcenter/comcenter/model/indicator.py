# -*- coding: utf-8 -*-
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

from sqlalchemy import schema as saschema 
from comcenter.model import DeclarativeBase, metadata, DBSession
from comcenter.model.auth import User;
#from sqlalchemy.sql.expression import *;
from comcenter.controllers.util.utility import Utility;
import logging;
import sys;
log = logging.getLogger(__name__);

__all__ = ['Years' ,'Months' ,'IndicatorsType','TargetYear' ,'IndicatorsGroup' ,'IndicatorsDetail'  ,'MapIndicatorsSection' , 'IndicatorsDetail' ,'IndicatorsService'];

class Months(DeclarativeBase):
    __tablename__ = 'months';
    months_id = Column(Integer, autoincrement=True, primary_key=True);
    month = Column(String(255), unique=True, nullable=False);
   
    def __init__(self):
        self.months_id = None;
        self.month = None;         
        
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
        return DBSession.query(cls).order_by(cls.months_id).all();
    
class Years(DeclarativeBase):
    __tablename__ = 'years';
    years_id = Column(Integer, autoincrement=True, primary_key=True);
    year = Column(String(255), unique=True, nullable=False);
   
    def __init__(self):
        self.years_id = None;
        self.year = None;         
        
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
        return DBSession.query(cls).order_by(cls.years_id).all();
    
    
    
     
    
   

class IndicatorsType(DeclarativeBase):
    __tablename__ = 'indicators_type';
    indicators_type_id = Column(Integer, autoincrement=True, primary_key=True);
    indicators_type_name = Column(String(255), unique=True, nullable=False);    
    active =  Column(String(1) , nullable=False,default =1);
   
    def __init__(self):
        self.months_id = None;
        self.month = None;         
        
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
        return DBSession.query(cls).order_by(cls.months_id).all();
 
        
class IndicatorsGroup(DeclarativeBase):
    __tablename__ = 'indicators_group';
    indicators_group_id = Column(Integer, autoincrement=True, primary_key=True);
    indicators_group_name = Column(String(255), unique=True, nullable=False);    
    
    indicators_type_id = Column(   Integer,ForeignKey('indicators_type.indicators_type_id'), nullable=False, index=True) ;
    indicators_type = relation('IndicatorsType', backref='indicatorstype');
    
    active =  Column(String(1) , nullable=False,default =1);
   
    def __init__(self):
        self.indicators_group_id = None;
        self.indicators_group_name = None;     
        self.indicators_type_id = 0;
        self.active ='1';
        
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
        return DBSession.query(cls).order_by(cls.months_id).all();
    
    


class IndicatorsDetail(DeclarativeBase):
    __tablename__ = 'indicators_detail';
    indicators_detail_id = Column(Integer, autoincrement=True, primary_key=True);
    detail = Column(   Text, nullable=False);  
    
    indicators_group_id = Column(   Integer,ForeignKey('indicators_group.indicators_group_id'), nullable=False, index=True) ;
    indicators_group = relation('IndicatorsGroup', backref='indicatorsdetail');
    
    active =  Column(String(1) , nullable=False,default =1);
   
    def __init__(self):
        self.indicators_group_id = None;
        self.indicators_group_name = None;     
        self.indicators_type_id = 0;
        self.active ='1';
        
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
        return DBSession.query(cls).order_by(cls.months_id).all();
    
   
  
class TargetYear(DeclarativeBase):
    __tablename__ = 'target_year';
    target_year_id = Column(Integer, autoincrement=True, primary_key=True);
    
    indicators_detail_id = Column(   Integer,ForeignKey('indicators_detail.indicators_detail_id'), nullable=False, index=True) ;
    indicators_detail = relation('IndicatorsDetail', backref='apIndicatorssection');
    
    years_id = Column(   Integer,ForeignKey('years.years_id'), nullable=False, index=True) ;
    years = relation('Years', backref='apIndicatorssection');
    
    target = Column(String(255), nullable=False);
    active =  Column(String(1) , nullable=False,default =1);
       
    def __init__(self):
        self.target_year_id = None;
        self.indicators_detail_id = 0; 
        self.years_id = 0;        
        self.target = 0;
        self.active = '1';
        
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
        return DBSession.query(cls).filter(  cls.active == 1 ).order_by(cls.years_id).all();  
    

class MapIndicatorsSection(DeclarativeBase):
    __tablename__ = 'map_indicators_section';
    
    map_indicators_section_id = Column(Integer, autoincrement=True, primary_key=True);
    indicators_detail_id = Column(   Integer,ForeignKey('indicators_detail.indicators_detail_id'), nullable=False, index=True) ;
    indicators_detail = relation('IndicatorsDetail', backref=',apIndicatorssection');
    
    risk_section_id = Column(   Integer,ForeignKey('risk_section.risk_section_id'), nullable=False, index=True) ;
    risk_section = relation('RiskSection', backref=',apIndicatorssection');
    
    def __init__(self):
        self.map_indicators_section_id = None;
        self.indicators_detail_id = 0;
        self.risk_section_id = 0;
    
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
      
class IndicatorsService(DeclarativeBase):
    __tablename__ = 'indicators_service';
    
    indicators_service_id = Column(Integer, autoincrement=True, primary_key=True);
    
    indicators_detail_id = Column(   Integer,ForeignKey('indicators_detail.indicators_detail_id'), nullable=False, index=True) ;
    indicators_detail = relation('IndicatorsDetail', backref='indicatorsService');
    
    years_id = Column(   Integer,ForeignKey('years.years_id'), nullable=False, index=True) ;
    years = relation('Years', backref='indicatorsService');
    
    months_id = Column(   Integer,ForeignKey('months.months_id'), nullable=False, index=True) ;
    months = relation('Months', backref='indicatorsService');
    
    
    risk_section_id = Column(   Integer,ForeignKey('risk_section.risk_section_id'), nullable=False, index=True) ;
    risk_section = relation('RiskSection', backref='indicatorsService');
    
    indicator_value = Column(String(255) , nullable=False);
    create_date  =  Column(DateTime, nullable=False, default=datetime.now);
    update_date  =  Column(DateTime, nullable=False, default=datetime.now);
    
    
    def __init__(self):
        self.indicators_service_id = None;
        self.indicators_detail_id = None;
       
        self.years_id = 0;
        self.months_id = 0;
        self.risk_section_id = 0;
        self.indicator_value =0;
        
        self.create_date =  datetime.now();
        self.update_date =  datetime.now();
    
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
    def listIndicatorBySection(cls,sectionid=None,year=None,start_year=None,month=None):
       
        list =[];
        if(sectionid ):
            sql = text("""select  
                                id.indicators_detail_id,
                                id.detail,
                                ty.target,
                                rs.risk_section_id,
                                rs.description,
                                ids.indicators_service_id,
                                ids.indicator_value,
                              ids.months_id,
                                ty.years_id
                             from 
                                indicators_detail id
                                LEFT JOIN target_year ty on id.indicators_detail_id = ty.indicators_detail_id
                                LEFT JOIN map_indicators_section mis on id.indicators_detail_id = mis.indicators_detail_id
                                LEFT JOIN risk_section rs on rs.risk_section_id = mis.risk_section_id
                                LEFT OUTER JOIN indicators_service ids on (ids.indicators_detail_id = id.indicators_detail_id 
                                             and ids.risk_section_id =rs.risk_section_id and ids.years_id = ty.years_id and ids.months_id = """   + str(month) +""" )
                                 
                            where
                                ty.active = 1
                                and ty.years_id = """ + str(year) + """  
                                and rs.risk_section_id = """ + str(sectionid) + """ 
    
                              """);
                              
            result = DBSession.execute(sql);
            
            for row in result:
                list.append({ 'id'  : row['indicators_detail_id']  ,
                              'indicators_detail_id'  : row['indicators_detail_id']  ,  
                              'indicators_service_id'  : row['indicators_service_id'],  
                                 'detail'  : row['detail']  , 
                                 'target'  : row['target']  ,
                                 'risk_section_id'  : row['risk_section_id']  ,
                                 'indicator_value'  : row['indicator_value']  ,
                                 'months_id'  : row['months_id']  ,
                                 'years_id'  : row['years_id']  });
            
            
        return list;
    
    @classmethod
    def listReport1Indicator1(cls,sectionid=None ,year=None,month = None):
        listHash = {};
        a=0;b=0;c=0;d=0;e=0;f=0;g=0;h=0;i=0;j=0;k=0;l=0;
        indictor = {   'indicators_service_id' : 1,  
                                        'detail' : 'test',  
                                        'target' : 0 ,  
                                        '1' : a,'2' : b,'3' : c,'4' : d,'5' : e,'6' : f,
                                        '7' : g,'8' : h,'9' : i,'10' : j,'11' : k,'12' : l      };      
        indictor2 = {   'indicators_service_id' : 2,  
                                        'detail' : 'test2',  
                                        'target' : 0 ,  
                                        '1' : a,'2' : b,'3' : c,'4' : d,'5' : e,'6' : f,
                                        '7' : g,'8' : h,'9' : i,'10' : j,'11' : k,'12' : l      };      
        indicators = {};
        indicators2 = {};
        indicators[1 ] = indictor;
        indicators2[1 ]= indictor;
        listHash[1] = {'id': 1, 'name'  :'test group 1',  'indicators' : indicators  };
        listHash[2] = {'id': 2, 'name'  :'test group 2',  'indicators' : indicators2  };
        
        result =  listHash.get(1);
        
        indicators =  result.get ('indicators');
        indictor =  indicators.get(2);
        if (indictor is None):
            indicators[2 ] = indictor2;
        result['indicators'] = indicators;
        listHash[1] = result ;
        
        return listHash;
    @classmethod
    def listReport1Indicator(cls,sectionid=None ,year=None,month = None):
        
        listHash = {};
        
        if(sectionid ):
             
                                
            sql = text(""" 
                    select 
                            ind.indicators_detail_id,
                            ind.indicators_group_id,
                            ing.indicators_group_name,
                            ind.detail,
                            ty.target,
                            mis.risk_section_id,
                            rs.description as section,
                         
                        (select  IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2),2),IsSpace(ins2.indicator_value)),'-' )   from indicators_service ins2 where ins2.months_id = 10 and ins2.years_id = (ty.years_id) and ins2.indicators_detail_id = ind.indicators_detail_id and ins2.risk_section_id = rs.risk_section_id  ) as "1",
                            (select  IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2),2),IsSpace(ins2.indicator_value)),'-' )  from indicators_service ins2 where ins2.months_id = 11 and ins2.years_id = (ty.years_id) and ins2.indicators_detail_id = ind.indicators_detail_id and ins2.risk_section_id = rs.risk_section_id   ) as "2",
                            (select  IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2),2),IsSpace(ins2.indicator_value)),'-' )   from indicators_service ins2 where ins2.months_id = 12 and ins2.years_id = (ty.years_id) and ins2.indicators_detail_id = ind.indicators_detail_id and ins2.risk_section_id = rs.risk_section_id   ) as "3",
                            (select  IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2),2),IsSpace(ins2.indicator_value)),'-' )  from indicators_service ins2 where ins2.months_id = 1 and ins2.years_id = (ty.years_id) and ins2.indicators_detail_id = ind.indicators_detail_id  and ins2.risk_section_id = rs.risk_section_id  ) as "4",
                            (select  IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2),2),IsSpace(ins2.indicator_value)),'-' )  from indicators_service ins2 where ins2.months_id = 2 and ins2.years_id = (ty.years_id) and ins2.indicators_detail_id = ind.indicators_detail_id and ins2.risk_section_id = rs.risk_section_id  ) as "5",
                            (select  IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2),2),IsSpace(ins2.indicator_value)),'-' )   from indicators_service ins2 where ins2.months_id = 3 and ins2.years_id = (ty.years_id) and ins2.indicators_detail_id = ind.indicators_detail_id and ins2.risk_section_id = rs.risk_section_id  ) as "6",
                            (select  IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2),2),IsSpace(ins2.indicator_value)),'-' )  from indicators_service ins2 where ins2.months_id = 4 and ins2.years_id = (ty.years_id) and ins2.indicators_detail_id = ind.indicators_detail_id and ins2.risk_section_id = rs.risk_section_id  ) as "7",
                            (select  IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2),2),IsSpace(ins2.indicator_value)),'-' )   from indicators_service ins2 where ins2.months_id = 5 and ins2.years_id = (ty.years_id) and ins2.indicators_detail_id = ind.indicators_detail_id and ins2.risk_section_id = rs.risk_section_id  ) as "8",
                            (select  IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2),2),IsSpace(ins2.indicator_value)),'-' )  from indicators_service ins2 where ins2.months_id = 6 and ins2.years_id = (ty.years_id) and ins2.indicators_detail_id = ind.indicators_detail_id and ins2.risk_section_id = rs.risk_section_id  ) as "9",
                            (select  IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2),2),IsSpace(ins2.indicator_value)),'-' )  from indicators_service ins2 where ins2.months_id = 7 and ins2.years_id = (ty.years_id) and ins2.indicators_detail_id = ind.indicators_detail_id and ins2.risk_section_id = rs.risk_section_id   ) as "10",
                            (select  IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2),2),IsSpace(ins2.indicator_value)),'-' )  from indicators_service ins2 where ins2.months_id = 8 and ins2.years_id = (ty.years_id) and ins2.indicators_detail_id = ind.indicators_detail_id and ins2.risk_section_id = rs.risk_section_id  ) as "11",
                            (select  IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2),2),IsSpace(ins2.indicator_value)),'-' )   from indicators_service ins2 where ins2.months_id = 9 and ins2.years_id = (ty.years_id) and ins2.indicators_detail_id = ind.indicators_detail_id and ins2.risk_section_id = rs.risk_section_id  ) as "12"
                    from 
                            indicators_detail ind LEFT JOIN target_year ty on ind.indicators_detail_id = ty.indicators_detail_id
                            LEFT JOIN indicators_group ing on ing.indicators_group_id = ind.indicators_group_id
                            LEFT JOIN map_indicators_section mis on mis.indicators_detail_id =  ind.indicators_detail_id
                            LEFT JOIN risk_section rs on rs.risk_section_id = mis.risk_section_id
                             
                    where 
                            -- mis.risk_section_id = 11 and
                            ind.active =1 and ing.active =1 and
                            ty.active = 1 and
                            rs.risk_section_id = """ + str( sectionid) + """
                                  and ty.years_id = """ +  str(year) +"""
                """);

            result = DBSession.execute(sql);
            ulit =  Utility();
            for row in result:
                
                rs = listHash.get(row['indicators_group_id']);
                
                 
                #a=0;b=0;c=0;d=0;e=0;f=0;g=0;h=0;i=0;j=0;k=0;l=0;
                a='-' ;b= '-'  ;c= '-'  ;d= '-'  ;e= '-'  ;f= '-'  ;g= '-'  ;h= '-'  ;i= '-'  ;j= '-'  ;k= '-'  ;l= '-'  ;
                a = ulit.numValue(row['1']);
                b = ulit.numValue(row['2']);
                c = row['3']; #ulit.numValue(row['3']);
                d = ulit.numValue(row['4']);
                e = ulit.numValue(row['5']);
                f = ulit.numValue(row['6']);
                g = ulit.numValue(row['7']);
                h = ulit.numValue(row['8']);
                i = ulit.numValue(row['9']);
                j = ulit.numValue(row['10']);
                k = ulit.numValue(row['11']);
                l = ulit.numValue(row['12']);
                
                
                
                if(rs is None):
                  
                    indictor = {   'indicators_detail_id' : row['indicators_detail_id'],  
                                        'detail' : row['detail'],  
                                        'target' : row['target'],  
                                        '1' : a,'2' : b,'3' : c,'4' : d,'5' : e,'6' : f,
                                        '7' : g,'8' : h,'9' : i,'10' : j,'11' : k,'12' : l     
                                      };
                    
                    indicators = {};
                    indicators[row['indicators_detail_id'] ] = indictor;
                    
                    listHash[row['indicators_group_id']] = {'id': row['indicators_group_id'], 'name'  : row['indicators_group_name'] , 'indicators' : indicators  };
                else:
                    
                    indicators_group_id =  rs['id']  ;
               
                     
                    
                    indicators1 =  rs.get ('indicators');
                     
                    
                    
                    
                    indictor1 = {   'indicators_detail_id' : row['indicators_detail_id'],  
                                        'detail' : row['detail'],  
                                        'target' : row['target'],  
                                        '1' : a,'2' : b,'3' : c,'4' : d,'5' : e,'6' : f,
                                        '7' : g,'8' : h,'9' : i,'10' : j,'11' : k,'12' : l     
                                      };
                    indicators1[ row['indicators_detail_id']  ]    = indictor1;
                                   
                    rs['indicators'] = indicators1;
                      
                    listHash[row['indicators_group_id']] = rs ;
                         
                    #indictor1 =  indicators1.get(row['indicators_detail_id'] );
                
             
                 
        return listHash;
    
    
    @classmethod
    def listReport2Indicator(cls ,year=None ):
        listGroupHash = {};
        sql = text("""select
				ind_type.indicators_type_id,
				ind_type.indicators_type_name,
                                ind.indicators_detail_id,
                                ind.indicators_group_id,
                                ing.indicators_group_name,
                                ind.detail,
                                ty.target,
                                mis.risk_section_id,
                                rs.description as section,
                                                            case when mis.risk_section_id in (3,4) THEN 
                                                                     (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2)/2,2),IsSpace(ins2.indicator_value)),'-' )    from indicators_service ins2 where ins2.months_id = 10 and ins2.years_id = (ty.years_id) and ins2.indicators_detail_id = ind.indicators_detail_id    ) 
                                                                     else (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(sum(ins2.indicator_value),2),IsSpace(ins2.indicator_value)),'-' )   from indicators_service ins2 where ins2.months_id = 10 and ins2.years_id = (ty.years_id) and ins2.indicators_detail_id = ind.indicators_detail_id    )  end  as "1",
                                                            case when mis.risk_section_id in (3,4) THEN 
                                                                     (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2)/2,2),IsSpace(ins2.indicator_value)),'-' )    from indicators_service ins2 where ins2.months_id = 11 and ins2.years_id = (ty.years_id) and ins2.indicators_detail_id = ind.indicators_detail_id    ) 
                                                                     else (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(sum(ins2.indicator_value),2),IsSpace(ins2.indicator_value)),'-' )   from indicators_service ins2 where ins2.months_id = 11 and ins2.years_id = (ty.years_id) and ins2.indicators_detail_id = ind.indicators_detail_id    )  end  as "2",
                                                            case when mis.risk_section_id in (3,4) THEN 
                                                                     (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2)/2,2),IsSpace(ins2.indicator_value)),'-' )    from indicators_service ins2 where ins2.months_id = 12 and ins2.years_id = (ty.years_id) and ins2.indicators_detail_id = ind.indicators_detail_id    ) 
                                                                     else (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(sum(ins2.indicator_value),2),IsSpace(ins2.indicator_value)),'-' )   from indicators_service ins2 where ins2.months_id = 12 and ins2.years_id = (ty.years_id) and ins2.indicators_detail_id = ind.indicators_detail_id    )  end  as "3",
                                                            case when mis.risk_section_id in (3,4) THEN 
                                                                     (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2)/2,2),IsSpace(ins2.indicator_value)),'-' )    from indicators_service ins2 where ins2.months_id = 1 and ins2.years_id = ty.years_id and ins2.indicators_detail_id = ind.indicators_detail_id    ) 
                                                                     else (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(sum(ins2.indicator_value),2),IsSpace(ins2.indicator_value)),'-' )   from indicators_service ins2 where ins2.months_id = 1 and ins2.years_id = ty.years_id and ins2.indicators_detail_id = ind.indicators_detail_id    )  end  as "4",
                                                            case when mis.risk_section_id in (3,4) THEN 
                                                                     (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2)/2,2),IsSpace(ins2.indicator_value)),'-' )    from indicators_service ins2 where ins2.months_id = 2 and ins2.years_id = ty.years_id and ins2.indicators_detail_id = ind.indicators_detail_id    ) 
                                                                     else (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(sum(ins2.indicator_value),2),IsSpace(ins2.indicator_value)),'-' )   from indicators_service ins2 where ins2.months_id = 2 and ins2.years_id = ty.years_id and ins2.indicators_detail_id = ind.indicators_detail_id    )  end  as "5",
                                                            case when mis.risk_section_id in (3,4) THEN 
                                                                     (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2)/2,2),IsSpace(ins2.indicator_value)),'-' )    from indicators_service ins2 where ins2.months_id = 3 and ins2.years_id = ty.years_id and ins2.indicators_detail_id = ind.indicators_detail_id    ) 
                                                                     else (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(sum(ins2.indicator_value),2),IsSpace(ins2.indicator_value)),'-' )   from indicators_service ins2 where ins2.months_id = 3 and ins2.years_id = ty.years_id and ins2.indicators_detail_id = ind.indicators_detail_id    )  end  as "6",
                                                            case when mis.risk_section_id in (3,4) THEN 
                                                                     (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2)/2,2),IsSpace(ins2.indicator_value)),'-' )    from indicators_service ins2 where ins2.months_id = 4 and ins2.years_id = ty.years_id and ins2.indicators_detail_id = ind.indicators_detail_id    ) 
                                                                     else (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(sum(ins2.indicator_value),2),IsSpace(ins2.indicator_value)),'-' )   from indicators_service ins2 where ins2.months_id = 4 and ins2.years_id = ty.years_id and ins2.indicators_detail_id = ind.indicators_detail_id    )  end  as "7",
                                                            case when mis.risk_section_id in (3,4) THEN 
                                                                     (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1, ROUND(ROUND(sum(ins2.indicator_value),2)/2,2),IsSpace(ins2.indicator_value)),'-' )    from indicators_service ins2 where ins2.months_id = 5 and ins2.years_id = ty.years_id and ins2.indicators_detail_id = ind.indicators_detail_id    ) 
                                                                     else (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1, ROUND(sum(ins2.indicator_value),2),IsSpace(ins2.indicator_value)) ,'-' )   from indicators_service ins2 where ins2.months_id = 5 and ins2.years_id = ty.years_id and ins2.indicators_detail_id = ind.indicators_detail_id    )  end  as "8",
                                                            case when mis.risk_section_id in (3,4) THEN 
                                                                     (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2)/2,2),IsSpace(ins2.indicator_value)),'-' )    from indicators_service ins2 where ins2.months_id = 6 and ins2.years_id = ty.years_id and ins2.indicators_detail_id = ind.indicators_detail_id    ) 
                                                                     else (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(sum(ins2.indicator_value),2),IsSpace(ins2.indicator_value)),'-' )   from indicators_service ins2 where ins2.months_id = 6 and ins2.years_id = ty.years_id and ins2.indicators_detail_id = ind.indicators_detail_id    )  end  as "9",
                                                            case when mis.risk_section_id in (3,4) THEN 
                                                                     (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2)/2,2),IsSpace(ins2.indicator_value)),'-' )    from indicators_service ins2 where ins2.months_id = 7 and ins2.years_id = ty.years_id and ins2.indicators_detail_id = ind.indicators_detail_id    ) 
                                                                     else (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(sum(ins2.indicator_value),2),IsSpace(ins2.indicator_value)),'-' )   from indicators_service ins2 where ins2.months_id = 7 and ins2.years_id = ty.years_id and ins2.indicators_detail_id = ind.indicators_detail_id    )  end  as "10",
                                                            case when mis.risk_section_id in (3,4) THEN 
                                                                     (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2)/2,2),IsSpace(ins2.indicator_value)),'-' )    from indicators_service ins2 where ins2.months_id = 8 and ins2.years_id = ty.years_id and ins2.indicators_detail_id = ind.indicators_detail_id    ) 
                                                                     else (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(sum(ins2.indicator_value),2),IsSpace(ins2.indicator_value)),'-' )   from indicators_service ins2 where ins2.months_id = 8 and ins2.years_id = ty.years_id and ins2.indicators_detail_id = ind.indicators_detail_id    )  end  as "11",
                                                            case when mis.risk_section_id in (3,4) THEN 
                                                                     (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(ROUND(sum(ins2.indicator_value),2)/2,2),IsSpace(ins2.indicator_value)),'-' )    from indicators_service ins2 where ins2.months_id = 9 and ins2.years_id = ty.years_id and ins2.indicators_detail_id = ind.indicators_detail_id    ) 
                                                                     else (select IFNULL(  IF (IsNumeric(ins2.indicator_value)= 1,ROUND(sum(ins2.indicator_value),2),IsSpace(ins2.indicator_value)),'-' )   from indicators_service ins2 where ins2.months_id = 9 and ins2.years_id = ty.years_id and ins2.indicators_detail_id = ind.indicators_detail_id    )  end  as "12"
                              
 
                        from 
                                indicators_detail ind LEFT JOIN target_year ty on ind.indicators_detail_id = ty.indicators_detail_id
                                LEFT JOIN indicators_group ing on ing.indicators_group_id = ind.indicators_group_id
                                LEFT JOIN indicators_type ind_type on ind_type.indicators_type_id  = ing.indicators_type_id
                                LEFT JOIN map_indicators_section mis on mis.indicators_detail_id =  ind.indicators_detail_id
                                LEFT JOIN risk_section rs on rs.risk_section_id = mis.risk_section_id
                                 
                          
                        where 
                            ind.active =1 and ing.active =1
                            and ty.active = 1 
                            and ty.years_id = """ +  str(year) +"""
        """);
        
        result = DBSession.execute(sql);
        
        ulit =  Utility();
        for row in result:
            rsGroupType = listGroupHash.get(row['indicators_type_id']);

            a='-' ;b= '-'  ;c= '-'  ;d= '-'  ;e= '-'  ;f= '-'  ;g= '-'  ;h= '-'  ;i= '-'  ;j= '-'  ;k= '-'  ;l= '-'  ;
            a = ulit.numValue(row['1']);
            b = ulit.numValue(row['2']);
            c = ulit.numValue(row['3']);
            d = ulit.numValue(row['4']);
            e = ulit.numValue(row['5']);
            f = ulit.numValue(row['6']);
            g = ulit.numValue(row['7']);
            h = ulit.numValue(row['8']);
            i = ulit.numValue(row['9']);
            j = ulit.numValue(row['10']);
            k = ulit.numValue(row['11']);
            l = ulit.numValue(row['12']);
            
            if(rsGroupType is None):
                
                                        
                indictor = {   'indicators_detail_id' : row['indicators_detail_id'],  
                                'detail' : row['detail'],  
                                'target' : row['target'],  
                                '1' : a,'2' : b,'3' : c,'4' : d,'5' : e,'6' : f,
                                '7' : g,'8' : h,'9' : i,'10' : j,'11' : k,'12' : l     
                            };
                        
                indicators = {};
                indicators[row['indicators_detail_id'] ] = indictor;
                indicators0 = {};        
                indicators0[row['indicators_group_id']] = {'id': row['indicators_group_id'], 'name'  : row['indicators_group_name'] , 'indicators' : indicators  };
                                        
                listGroupHash[row['indicators_type_id']] = {'id': row['indicators_group_id'], 'name'  : row['indicators_type_name'] , 'indicators_group' : indicators0  };
                                
            else:
                group_type = rsGroupType['id'];
                indicators0 = rsGroupType.get('indicators_group');

                if(indicators0 is None):
                    
                    pass;
                else:
                    group = indicators0.get(row['indicators_group_id']);

                    if(group is None):

                        indictor = {   'indicators_detail_id' : row['indicators_detail_id'],  
                                'detail' : row['detail'],  
                                'target' : row['target'],  
                                '1' : a,'2' : b,'3' : c,'4' : d,'5' : e,'6' : f,
                                '7' : g,'8' : h,'9' : i,'10' : j,'11' : k,'12' : l     
                            };
                        
                        indicators = {};
                        indicators[row['indicators_detail_id'] ] = indictor;
                         
                        indicators0[ row['indicators_group_id'] ] = {'id': row['indicators_group_id'], 'name'  : row['indicators_group_name'] , 'indicators' : indicators  };

                    else:
                        indicators_group = group['id'];
                        indicators = group['indicators'];

                        indictor1 = {   'indicators_detail_id' : row['indicators_detail_id'],  
                                        'detail' : row['detail'],  
                                        'target' : row['target'],  
                                        '1' : a,'2' : b,'3' : c,'4' : d,'5' : e,'6' : f,
                                        '7' : g,'8' : h,'9' : i,'10' : j,'11' : k,'12' : l     
                                      };
                        indicators[ row['indicators_detail_id']  ]    = indictor1;
                        group['indicators'] = indicators;
                        indicators0[row['indicators_group_id']] = group;

        return listGroupHash;
    
