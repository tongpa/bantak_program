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

__all__ = ['MaintenanceStatus',    'MaintenanceType','Maintenance','MaintenaceUserStatus']

class MaintenanceStatus(DeclarativeBase):
    __tablename__ = 'maintenance_status'
    mtn_status_id =  Column(Integer, autoincrement=True, primary_key=True);
    description =  Column(String(255), unique=True, nullable=False);
    
    def __init__(self):
        self.mtn_status_id = None;
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
    
     

    
class MaintenanceType(DeclarativeBase):
    __tablename__ = 'maintenance_type'
    
    mtn_type_id =  Column(Integer, autoincrement=True, primary_key=True);
    description =  Column(String(255), unique=True, nullable=False);
    
    def __init__(self):
        self.mtn_type_id = None;
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
    

class Maintenance(DeclarativeBase):
    
    __tablename__ = 'maintenance'
    
    maintenance_id = Column(Integer, autoincrement=True, primary_key=True);
    user_id = Column(   Integer,ForeignKey('tg_user.user_id'), nullable=False, index=True) ;
    mtn_type_id = Column(Integer,ForeignKey('maintenance_type.mtn_type_id'),nullable=False, default=1  );
    division_id = Column(Integer,ForeignKey('division.division_id'),nullable=False, default=1  );
    detail = Column(   Text, nullable=False);
    mtn_status_id  = Column(Integer,ForeignKey('maintenance_status.mtn_status_id'),nullable=False, default=1  );
    result_detail = Column(   Text, nullable=False);
    created = Column(DateTime, default=datetime.now);
    receipt_date = Column(DateTime );
    
    def __init__(self):
        self.maintenance_id = None;
        self.user_id = None;
        self.mtn_type_id = None;
        self.division_id = None;
        self.detail = None;
        self.mtn_status_id = None;
        self.result_detail = None;
        self.created =  datetime.now();
        self.receipt_date = None;
        
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



class MaintenaceUserStatus(DeclarativeBase):
    __tablename__ = 'maintenance_user_status'
    mtnuser_status_id =  Column(Integer, autoincrement=True, primary_key=True);
    user_id = Column(   Integer,ForeignKey('tg_user.user_id'), nullable=False, index=True) ;
    maintenance_id = Column(Integer,ForeignKey('maintenance.maintenance_id'),nullable=False, default=1  );
    mtn_status_id  = Column(Integer,ForeignKey('maintenance_status.mtn_status_id'),nullable=False, default=1  );
    created = Column(DateTime, default=datetime.now);
    
    
    def __init__(self):
        self.mtnuser_status_id = None;
        self.user_id = None;
        self.maintenance_id = None;
        self.mtn_status_id = None;
        self.created =  datetime.now();
        
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
    