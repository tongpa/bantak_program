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
from sqlalchemy.types import Unicode, Integer, DateTime, String, Text, Float
from sqlalchemy.orm import relation, synonym
from sqlalchemy import *;
from comcenter.model import DeclarativeBase, metadata, DBSession
#from sqlalchemy.sql.expression import *;
import logging;
import sys;
log = logging.getLogger(__name__);

__all__ = ['School', 'SchoolClass', 'DentalSchoolService','DentalSchoolKpi','DentalSchoolKpiGroup',
           'SeniorClub','DentalSeniorClubKpi','DentalSeniorClubService',
           'ChildDevCenter', 'DentalChildDevCenterKpi','DentalChildDevCenterService' ]

class School(DeclarativeBase):
    __tablename__ = 'school';
    school_id = Column(Integer, autoincrement=True, primary_key=True);
    school_name = Column(String(255), unique=True, nullable=False);
    school_address = Column(String(255),  nullable=False);
    latitude  = Column(Float,   nullable=False);
    longitude = Column(Float,   nullable=False);
    high_school = Column(String(1), unique=False, nullable=False, default= 0);
    def __init__(self):
        self.school_id = None;
        self.school_name = None;
        self.school_address = None;
        self.latitude = None;
        self.longitude = None; 
        self.high_school = 0;
        
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
    def listPrimarySchool(cls):
        return DBSession.query(cls).filter(  cls.high_school==str(0) ).order_by(cls.school_id).all();
    @classmethod
    def listAll(cls):
        return DBSession.query(cls).order_by(cls.school_id).all();
    

class SchoolClass(DeclarativeBase):
    __tablename__ = 'school_class';
    school_class_id = Column(Integer, autoincrement=True, primary_key=True);
    school_class_name = Column(String(255), unique=True, nullable=False);
     
    
    def __init__(self):
        self.school_class_id = None;
        self.school_class_name = None;
         
        
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
        return DBSession.query(cls).order_by(cls.school_class_id).all();

class DentalSchoolKpiGroup(DeclarativeBase):
    __tablename__ = 'dental_school_kpi_group';
    dental_school_kpi_group_id = Column(Integer, autoincrement=True, primary_key=True);
    detail = Column(String(255), unique=True, nullable=False);
   
    def __init__(self):
        self.dental_school_kpi_group_id = None;
        self.detail = None;
         
        
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
        return DBSession.query(cls).order_by(cls.dental_school_kpi_group_id).all();
            
class DentalSchoolKpi(DeclarativeBase):
    __tablename__ = 'dental_school_kpi';
    dental_school_kpi_id = Column(Integer, autoincrement=True, primary_key=True);
    detail = Column(String(255), unique=False, nullable=False);
    range  = Column(String(255), unique=False, nullable=False);
    dental_school_kpi_group_id  = Column(   Integer,ForeignKey('dental_school_kpi_group.dental_school_kpi_group_id'), nullable=False, index=True) ;
    dental_school_kpi_group  = relation('DentalSchoolKpiGroup', backref='DentalSchoolKpi');
    def __init__(self):
        self.dental_school_kpi_id = None;
        self.detail = None;
        self.range = None; 
        self.dental_school_kpi_group_id = None;
        
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
        return DBSession.query(cls).order_by(cls.dental_school_kpi_id).all();
    
    @classmethod
    def listkpibygroup(cls,group):
        return DBSession.query(cls).filter(  cls.dental_school_kpi_group_id==str(group) ).order_by(cls.dental_school_kpi_id ).all();
    
    
class DentalSchoolService(DeclarativeBase):
    __tablename__ = 'dental_school_service';
    dental_school_service_id = Column(Integer, autoincrement=True, primary_key=True);
    school_id  = Column(   Integer,ForeignKey('school.school_id'), nullable=False, index=True) ;
    school  = relation('School', backref='dentalschoolservice');
    dental_school_kpi_id  = Column(   Integer,ForeignKey('dental_school_kpi.dental_school_kpi_id'), nullable=False, index=True) ;
    dental_school_kpi  = relation('DentalSchoolKpi', backref='dentalschoolservice');
    fiscal_year =   Column(String(4), index=True,  nullable=False);    
    value =   Column(   Float(precision=2) , nullable=True, default= 0) ;
    school_class_id  = Column(   Integer,ForeignKey('school_class.school_class_id'), nullable=False, index=True) ;
    school_class  = relation('SchoolClass', backref='dentalschoolservice');
    
    
    def __init__(self):
        self.dental_school_service_id = None;
        self.school_id  = None;
        self.dental_school_kpi_id = None;
         
        self.fiscal_year = None;
        self.value =0;
        self.school_class_id  = None;
         
        
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
        return DBSession.query(cls).order_by(cls.dental_school_kpi_id).all();
    
    @classmethod
    def serviceShoAllKPIBySchool(cls,fiscalyear=None):
        sql = text("""
                select 
                    school.school_id,
                    school.school_name,
                    ( SELECT value from dental_school_service where  fiscal_year=:fiscal_year1 and dental_school_kpi_id = 2 and dental_school_service.school_id = school.school_id) as kpi1,
                    ( SELECT value from dental_school_service where  fiscal_year=:fiscal_year2 and dental_school_kpi_id = 3 and dental_school_service.school_id = school.school_id) as kpi2,
                    ( SELECT value from dental_school_service where  fiscal_year=:fiscal_year3 and dental_school_kpi_id = 4 and dental_school_service.school_id = school.school_id) as kpi3,
                    ( SELECT value from dental_school_service where  fiscal_year=:fiscal_year4 and dental_school_kpi_id = 9 and dental_school_service.school_id = school.school_id) as kpi4
                from 
                    school 
                WHERE
                    school.high_school = 0 
                ORDER BY 
                    school.school_id
            """, bindparams=[ bindparam('fiscal_year1', str(fiscalyear)),bindparam('fiscal_year2', str(fiscalyear)),bindparam('fiscal_year3', str(fiscalyear)),bindparam('fiscal_year4', str(fiscalyear)) ]);
        result = DBSession.execute(sql );
        return result ;
    
    @classmethod
    def serviceShowBySchoolandGroupKPI(cls,school=None,fiscalyear=None,groupKPI=None):
        sql = text("""SELECT
                    dental_school_kpi.dental_school_kpi_id,
                    dental_school_kpi.dental_school_kpi_group_id,
                    dental_school_kpi.detail,
                    dental_school_kpi.`range`,
                    service.dental_school_service_id,
                    service.fiscal_year,
                    service.school_id,
                    IFNULL(service.`value`,0) as value
                from 
                    dental_school_kpi  LEFT JOIN (
                        select 
                            dental_school_service.dental_school_service_id,
                            dental_school_service.fiscal_year,
                            dental_school_service.school_id,
                            dental_school_service.`value` ,
                            dental_school_service.dental_school_kpi_id
                         from 
                        school  JOIN dental_school_service on school.school_id =     dental_school_service.school_id
                        WHERE    
                            school.school_id=:schoolid and dental_school_service.fiscal_year=:fiscal_year  
                    ) service on service.dental_school_kpi_id = dental_school_kpi.dental_school_kpi_id
                WHERE
                    dental_school_kpi.dental_school_kpi_group_id=:groupkpi """ , bindparams=[bindparam('schoolid', str(school)),bindparam('fiscal_year', str(fiscalyear)) ,bindparam('groupkpi', str(groupKPI)) ] );
        #log.info(sql);
        result = DBSession.execute(sql );
        return result ; #DBSession.query(cls).filter(sql).all();
    
    
class SeniorClub(DeclarativeBase):
    __tablename__ = 'senior_club';
    senior_club_id = Column(Integer, autoincrement=True, primary_key=True);
    senior_club_name = Column(String(255), nullable=False);
    
    def __init__(self):
        self.senior_club_id = None;
        self.senior_club_name = None;
         
        
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
        return DBSession.query(cls).order_by(cls.senior_club_id).all();
    
class DentalSeniorClubKpi(DeclarativeBase):
    __tablename__ = 'dental_senior_club_kpi';
    dental_senior_club_kpi_id = Column(Integer, autoincrement=True, primary_key=True);
    detail = Column(String(255), unique=False, nullable=False);
    range  = Column(String(255), unique=False, nullable=True);
    
    def __init__(self):
        self.dental_senior_club_kpi_id = None;
        self.detail = None;
        self.range = None; 
        
        
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
        return DBSession.query(cls).order_by(cls.dental_senior_club_kpi_id).all();
    
class DentalSeniorClubService(DeclarativeBase):
    __tablename__ = 'dental_senior_club_service';
    dental_senior_club_service_id = Column(Integer, autoincrement=True, primary_key=True);
    senior_club_id  = Column(   Integer,ForeignKey('senior_club.senior_club_id'), nullable=False, index=True) ;
    senior_club  = relation('SeniorClub', backref='dentalseniorclubservice');
    dental_senior_club_kpi_id  = Column(   Integer,ForeignKey('dental_senior_club_kpi.dental_senior_club_kpi_id'), nullable=False, index=True) ;
    dental_senior_club_kpi  = relation('DentalSeniorClubKpi', backref='dentalseniorclubservice');
    fiscal_year =   Column(String(4), index=True,  nullable=False);    
    value =   Column(   Float(precision=2) , nullable=True, default= 0) ;
    
    def __init__(self):
        self.dental_senior_club_service_id = None;
        self.senior_club_id  = None;
        self.dental_senior_club_kpi_id = None;
        self.fiscal_year  = None;
        self.value = 0;
         
        
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
        return DBSession.query(cls).order_by(cls.dental_senior_club_service_id).all();
    
    @classmethod
    def serviceShowAllKPIBySenior(cls,fiscalyear=None):
        sql = text ("""
                SELECT
                    senior_club.senior_club_id,
                    senior_club.senior_club_name,
                    (SELECT value from dental_senior_club_service where fiscal_year =:fiscal_year1 and dental_senior_club_kpi_id = 2 and senior_club_id = senior_club.senior_club_id ) as kpi1,
                    (SELECT value from dental_senior_club_service where fiscal_year =:fiscal_year2 and dental_senior_club_kpi_id = 3 and senior_club_id = senior_club.senior_club_id ) as kpi2,
                    (SELECT value from dental_senior_club_service where fiscal_year =:fiscal_year3 and dental_senior_club_kpi_id = 4 and senior_club_id = senior_club.senior_club_id ) as kpi3
                FROM
                    senior_club
            """, bindparams=[bindparam('fiscal_year1', str(fiscalyear)),bindparam('fiscal_year2', str(fiscalyear)),bindparam('fiscal_year3', str(fiscalyear))  ]);
        result = DBSession.execute(sql );
        return result ;
    @classmethod
    def serviceShowByClub(cls,seniorclub=None,fiscalyear=None ):
        sql = text("""SELECT
                    dental_senior_club_kpi.dental_senior_club_kpi_id,
                    dental_senior_club_kpi.detail,
                    dental_senior_club_kpi.`range`,
                    senior_service.dental_senior_club_service_id,
                    senior_service.fiscal_year,
                    senior_service.senior_club_id,
                    IFNULL( senior_service.`value`, 0) as value
                    
                FROM
                    dental_senior_club_kpi LEFT JOIN 
                    (
                        SELECT    
                            senior_club.senior_club_id,
                            senior_club.senior_club_name,
                            dental_senior_club_service.fiscal_year,
                            dental_senior_club_service.`value`,
                            dental_senior_club_service.dental_senior_club_service_id,
                            dental_senior_club_service.dental_senior_club_kpi_id
                        from 
                            senior_club LEFT JOIN dental_senior_club_service on senior_club.senior_club_id = dental_senior_club_service.senior_club_id 
                        WHERE    
                            dental_senior_club_service.fiscal_year=:fiscal_year and 
                            senior_club.senior_club_id=:seniorclub
                    ) senior_service on dental_senior_club_kpi.dental_senior_club_kpi_id = senior_service.dental_senior_club_kpi_id
                 """ , bindparams=[bindparam('seniorclub', str(seniorclub)),bindparam('fiscal_year', str(fiscalyear))  ] );
        #log.info(sql);
        result = DBSession.execute(sql );
        return result ; #DBSession.query(cls).filter(sql).all();
    
class ChildDevCenter(DeclarativeBase):
    __tablename__ = 'child_dev_center';
    child_dev_center_id = Column(Integer, autoincrement=True, primary_key=True);
    child_dev_name = Column(String(255), nullable=False);
    
    def __init__(self):
        self.child_dev_center_id = None;
        self.child_dev_name = None;
         
        
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
        return DBSession.query(cls).order_by(cls.child_dev_center_id).all();
    
class DentalChildDevCenterKpi(DeclarativeBase):
    __tablename__ = 'dental_child_dev_center_kpi';
    dental_child_dev_center_kpi_id = Column(Integer, autoincrement=True, primary_key=True);
    detail = Column(String(255), unique=False, nullable=False);
    range  = Column(String(255), unique=False, nullable=True);
    
    def __init__(self):
        self.dental_child_dev_center_kpi_id = None;
        self.detail = None;
        self.range = None; 
        
        
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
        return DBSession.query(cls).order_by(cls.dental_child_dev_center_kpi_id).all();
    
class DentalChildDevCenterService(DeclarativeBase):
    __tablename__ = 'dental_child_dev_center_service';
    dental_child_dev_center_service_id = Column(Integer, autoincrement=True, primary_key=True);
    child_dev_center_id  = Column(   Integer,ForeignKey('child_dev_center.child_dev_center_id'), nullable=False, index=True) ;
    child_dev_center  = relation('ChildDevCenter', backref='denltalchilddevcenterservice');
    dental_child_dev_center_kpi_id  = Column(   Integer,ForeignKey('dental_child_dev_center_kpi.dental_child_dev_center_kpi_id'), nullable=False, index=True) ;
    dental_child_dev_center_kpi  = relation('DentalChildDevCenterKpi', backref='dentalchilddevcenterservice');
    fiscal_year =   Column(String(4), index=True,  nullable=False);    
    value =   Column(   Float(precision=2) , nullable=True, default= 0) ;
    
    def __init__(self):
        self.dental_child_dev_center_service_id = None;
        self.child_dev_center_id  = None;
        self.dental_child_dev_center_kpi_id = None;
         
         
        self.fiscal_year  = None;
        self.value = 0;
         
        
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
        return DBSession.query(cls).order_by(cls.dental_child_dev_center_service_id).all();
    
    @classmethod
    def serviceShoAllKPIByChildDevCenter(cls,fiscalyear=None):
        sql = text("""
            select 
                child_dev.child_dev_center_id,
                child_dev.child_dev_name,
                ( select value from dental_child_dev_center_service where fiscal_year =:fiscal_year1   and dental_child_dev_center_kpi_id =1 and dental_child_dev_center_service.child_dev_center_id = child_dev.child_dev_center_id) as kpi1,
                ( select value from dental_child_dev_center_service where fiscal_year =:fiscal_year2   and dental_child_dev_center_kpi_id =2 and dental_child_dev_center_service.child_dev_center_id = child_dev.child_dev_center_id) as kpi2
            from 
                child_dev_center as child_dev 
            ORDER BY 
                child_dev.child_dev_center_id
        """ , bindparams=[bindparam('fiscal_year1', str(fiscalyear)) ,bindparam('fiscal_year2', str(fiscalyear))  ]);
        result = DBSession.execute(sql );
        return result ;
    @classmethod
    def serviceShowByChildDevCenter(cls,childcenter=None,fiscalyear=None ):
        sql = text("""select 
                        dental_child_dev_center_kpi.dental_child_dev_center_kpi_id,
                        dental_child_dev_center_kpi.detail,
                        service.child_dev_center_id,
                        service.dental_child_dev_center_service_id,
                        service.fiscal_year,
                        IFNULL(service.`value`,0) as value
                    from 
                        dental_child_dev_center_kpi LEFT JOIN 
                        (
                            select 
                                dental_child_dev_center_service.child_dev_center_id,
                                dental_child_dev_center_service.dental_child_dev_center_service_id,
                                dental_child_dev_center_service.dental_child_dev_center_kpi_id,
                                dental_child_dev_center_service.fiscal_year,
                                dental_child_dev_center_service.`value`
                            FROM
                                child_dev_center LEFT JOIN dental_child_dev_center_service on dental_child_dev_center_service.child_dev_center_id = child_dev_center.child_dev_center_id
                            WHERE
                                dental_child_dev_center_service.fiscal_year=:fiscal_year and 
                                child_dev_center.child_dev_center_id=:childcenter
                        ) service on dental_child_dev_center_kpi.dental_child_dev_center_kpi_id = service.dental_child_dev_center_kpi_id
                 """ , bindparams=[bindparam('childcenter', str(childcenter)),bindparam('fiscal_year', str(fiscalyear))  ] );
        #log.info(sql);
        result = DBSession.execute(sql );
        return result ; #DBSession.query(cls).filter(sql).all();
    