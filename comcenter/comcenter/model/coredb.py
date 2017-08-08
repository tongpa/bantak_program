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

from comcenter.model import DeclarativeBase, metadata, DBSession

__all__ = [ 'Division', 'Department','Section']

class Division(DeclarativeBase):
    __tablename__ = 'division'
    division_id =  Column(Integer, autoincrement=True, primary_key=True);
    description =  Column(String(255), unique=True, nullable=False);
    
    def __init__(self):
        self.division_id = None;
        self.description = None;
        
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
    
class Department(DeclarativeBase):
    __tablename__ = 'department'
    department_id =  Column(Integer, autoincrement=True, primary_key=True);
    description =  Column(String(255), unique=True, nullable=False);
    
    def __init__(self):
        self.department_id = None;
        self.description = None;
        
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
    
class Section(DeclarativeBase):
    __tablename__ = 'section'
    section_id =  Column(Integer, autoincrement=True, primary_key=True);
    description =  Column(String(255), unique=True, nullable=False);
    division_id = Column(   Integer,ForeignKey('division.division_id'), nullable=False, index=True) ;  
    division  = relation('Division', backref='section');
    def __init__(self):
        self.department_id = None;
        self.description = None;
        self.division_id = None;
        
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
    def listByDivision(cls,division):
        return DBSession.query(cls).filter(  cls.division_id==str(division) ).order_by(cls.section_id ).all();
    @classmethod
    def listAll(cls):
        return DBSession.query(cls).all();