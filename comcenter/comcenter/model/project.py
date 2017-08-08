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
from comcenter.model import DeclarativeBase,DeclarativeBase2, metadata, DBSession, DBSession2
#from sqlalchemy.sql.expression import *;
import logging;
import sys;
log = logging.getLogger(__name__);

__all__ = ['ProjectStatus', 'ProjectType', 'Project','Plantype', 'TestSample']

class TestSample(DeclarativeBase2):
    __tablename__ = 'tg_user'
    
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    user_name = Column(Unicode(16), unique=True, nullable=False)
    email_address = Column(Unicode(255), unique=True, nullable=False)
    display_name = Column(Unicode(255))
    _password = Column('password', Unicode(128))
    created = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return ('<User: name=%s, email=%s, display=%s>' % (
                self.user_name, self.email_address, self.display_name)).encode('utf-8')
                
    @classmethod
    def selectAll(cls):
        return DBSession2.query(cls).order_by(cls.created).all();
    
class Plantype(DeclarativeBase):
    __tablename__ = 'plantype';
    plantype_id = Column(Integer, autoincrement=True, primary_key=True);
    plantype_name = Column(String(255), unique=True, nullable=False);
    
    def __init__(self):
        self.plantype_id = None;
        self.plantype_name = None;
        
    def save(self):
        DBSession.add(self); 
        DBSession.flush() ;
    
    def update(self):
        DBSession.update(self);
        
    def remove(self):
        DBSession.delete(self);
        DBSession.flush() ;
    
class ProjectStatus(DeclarativeBase):
    __tablename__ = 'project_status'
    project_status_id =  Column(Integer, autoincrement=True, primary_key=True);
    project_status_name =  Column(String(255), unique=True, nullable=False);
    
    def __init__(self):
        self.project_status_id = None;
        self.project_status_name = None;
        
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
        return DBSession.query(cls).order_by(cls.project_status_id).all();
    
class ProjectType(DeclarativeBase):
    __tablename__ = 'project_type'
    project_type_id =  Column(Integer, autoincrement=True, primary_key=True);
    project_type_name =  Column(String(255), unique=True, nullable=False);
    
    def __init__(self):
        self.project_type_id = None;
        self.project_type_name = None;
        
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
        return DBSession.query(cls).all();
    

class Project(DeclarativeBase):
    __tablename__ = 'project' 
    project_id =  Column(Integer, autoincrement=True, primary_key=True);
    project_name =  Column(String(255), index=True,  nullable=False);
    detail  = Column(   Text, nullable=False);
    budget =   Column(   Integer , nullable=True, default= 0) ;
    maintenance_funds_budget =   Column(   Integer , nullable=True, default= 0) ;
    budget_other = Column(   Integer , nullable=True, default= 0) ;
    budget_other_from = Column(   Text , nullable=True ) ;
    start_date  = Column(DateTime, nullable=False, default=datetime.now);
    stop_date  = Column(DateTime, nullable=True);
    actual_start_date =  Column(DateTime, nullable=True);
    actual_stop_date  = Column(DateTime, nullable=True);
    fiscal_year =   Column(String(4), index=True,  nullable=False);
    owner =   Column(String(255), nullable=False);
    create_date =  Column(DateTime, nullable=False, default=datetime.now);
    project_status_id = Column(   Integer,ForeignKey('project_status.project_status_id'), nullable=False, index=True) ; 
    project_status  = relation('ProjectStatus', backref='project');
    project_type_id  = Column(   Integer,ForeignKey('project_type.project_type_id'), nullable=False, index=True) ;
    project_type  = relation('ProjectType', backref='project');
    division_id = Column(   Integer,ForeignKey('division.division_id'), nullable=False, index=True) ;
    division  = relation('Division', backref='project');
    department_id = Column(   Integer,ForeignKey('department.department_id'), nullable=False, index=True) ;    
    department  = relation('Department', backref='project');
    section_id = Column(   Integer,ForeignKey('section.section_id'), nullable=False, index=True) ;
    section  = relation('Section', backref='project');
    plantype_id = Column(   Integer,ForeignKey('plantype.plantype_id'), nullable=False, index=True) ;
    plantype  = relation('Plantype', backref='project');
    def __init__(self):
        self.project_id =  None;
        self.project_name =  None;
        self.detail  = None;
        self.budget =  0;
        self.budget_other = 0;
        self.maintenance_funds_budget =0;
        self.budget_other_from = None;
        self.start_date   =  datetime.now();
        self.stop_date  = None;
        self.actual_start_date =  None;
        self.actual_stop_date  =None;
        self.owner =  None;
        self.create_date  =  datetime.now();
        self.project_status_id = 0; 
        self.project_type_id  = 0;
        self.division_id = 0;
        self.department_id = 0;    
        self.section_id =0;
        self.plantype_id =0;
        
        
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
    def search(cls,fiscalyear=None,division=None,section=None,status=None,projectType=None,start=0,limit=25):
        
        sql = "1=1 ";
        if (fiscalyear):
            sql = sql + " and fiscal_year = " + fiscalyear;
        if(projectType):
            sql = sql + " and project_type_id = " + projectType;
        if(division):
            sql = sql + " and division_id = " + division;
        if(section):
            sql = sql + " and section_id = " + section;
        if(status):
            sql = sql + " and project_status_id = " + status ;
            
        log.info(sql);
        return DBSession.query(cls).filter(sql).all();
         
     
    @classmethod
    def listAll(cls):
        return DBSession.query(cls).all();
    
    @classmethod
    def querySummary(cls,fiscalyear=None,division=None,section=None,status=None,projectType=None,start=0,limit=25):
        
        sql = "where 1=1 ";
        if (fiscalyear):
            sql = sql + " and project.fiscal_year = " + fiscalyear;
        if(projectType):
            sql = sql + " and project_type_id = " + projectType;
        if(division):
            sql = sql + " and project.division_id = " + division;
        if(section):
            sql = sql + " and project.section_id = " + section;
        if(status):
            sql = sql + " and project.project_status_id = " + status ;
        
        sql = text("""select 
                        d.description as division ,
                        sum( d.allbudget) as allbudget,
                        sum( d.budget) as budget,
                        sum( d.maintenance_funds_budget) as maintenance_funds_budget,
                        sum( d.budget_other_from) as budget_other_from
                      FROM
                        (
                            select 
                                division.description,
                                IFNULL(project.budget, 0) + IFNULL(project.maintenance_funds_budget,0) +IFNULL(project.budget_other_from ,0)  as allbudget,
                                IFNULL(project.budget, 0) as budget,
                                IFNULL(project.maintenance_funds_budget,0) as maintenance_funds_budget,
                                IFNULL(project.budget_other_from ,0) as  budget_other_from
                            from division left join project on division.division_id = project.division_id """ + sql +
                            
                   """     ) d
                    group by d.description """);
         
        result = DBSession.execute(sql);
         
        list = [];
        for row in result:
            
            list.append({ 'division':row['division'], 
                          'allBudget' :row['allbudget'] ,
                           'budget' :row['budget'] ,
                          'maintenance_funds_budget' :row['maintenance_funds_budget'] ,
                          'budget_other_from' :row['budget_other_from'],
                          u'งบประมาณ' :row['budget']  ,
                          u'งบประมาณอื่น' :row['budget_other_from']  ,
                          u'เงินบำรุง' :row['maintenance_funds_budget']  
                        });
           
        return list;    
        