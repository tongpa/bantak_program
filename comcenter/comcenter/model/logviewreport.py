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
import logging;
import sys;
log = logging.getLogger(__name__);

__all__ = ['ModuleView'  , 'LogviewReport'   ];

class ModuleView(DeclarativeBase):
    __tablename__ = 'module_view';
    module_view_id = Column(Integer, autoincrement=True, primary_key=True);
    description = Column(String(255), unique=True, nullable=False);
    
    def __init__(self):
        self.computer_type_id = None;
        self.description = None;
        
    def initData(self):
        self.data = ComputerTypes();
        self.data.description = 'Risk';
        self.data.save();
        
        self.data = ComputerTypes();
        self.data.description = 'KPI';
        self.data.save();
    
    def save(self):
        DBSession.add(self); 
        DBSession.flush() ;
    
    def update(self):
        DBSession.update(self);
        
    def remove(self):
        DBSession.delete(self);
        DBSession.flush() ;
        
    @classmethod
    def listAll(cls):
        return DBSession.query(cls).order_by(cls.description).all();
    
    
class LogviewReport(DeclarativeBase):
    __tablename__ = 'logview_report';
    logview_report_id = Column(Integer, autoincrement=True, primary_key=True);
    user = Column(String(255), unique=True, nullable=False);
    client_ip = Column(String(255), unique=True, nullable=False);
    
    module_view_id = Column(   Integer,ForeignKey('module_view.module_view_id'), nullable=False, index=True) ;
    module_view = relation('ModuleView', backref='logviewReport');
    view_datetime = Column(DateTime, nullable=False, default=datetime.now);
    
     
    
    def __init__(self):
        self.logview_report_id = None;
        self.user = None;
        self.client_ip = None;
        
        self.module_view_id = 0;        
        self.view_datetime =  datetime.now();
        
        
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
        return DBSession.query(cls) .get(str(id)); 
    
     
    def saveLogview(self, user,client_ip,module_view_id):
        self.view = LogviewReport();
        self.view.user = user;
        self.view.client_ip = client_ip;
        self.view.module_view_id = module_view_id;
        self.view.view_datetime =  datetime.now();
        
        self.view.save();
        
       