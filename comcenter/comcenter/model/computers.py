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

__all__ = ['ComputerTypes'  , 'CardTypes'  , 'ComputerIPMac'  ,  'Computers'  ];

class ComputerTypes(DeclarativeBase):
    __tablename__ = 'computer_types';
    computer_types_id = Column(Integer, autoincrement=True, primary_key=True);
    description = Column(String(255), unique=True, nullable=False);
    
    def __init__(self):
        self.computer_type_id = None;
        self.description = None;
    
    def initData(self):
        self.data = ComputerTypes();
        self.data.description = 'pc';
        self.data.save();
        
        self.data = ComputerTypes();
        self.data.description = 'notebook';
        self.data.save();
        
        self.data = ComputerTypes();
        self.data.description = 'printer';
        self.data.save();
        
        self.data = ComputerTypes();
        self.data.description = 'server';
        self.data.save();
        
        self.data = ComputerTypes();
        self.data.description = 'router';
        self.data.save();
        
        self.data = ComputerTypes();
        self.data.description = 'switch';
        self.data.save();
        
        self.data = ComputerTypes();
        self.data.description = 'hub';
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
    
class CardTypes(DeclarativeBase):
    __tablename__ = 'card_types';
    card_types_id = Column(Integer, autoincrement=True, primary_key=True);
    description = Column(String(255), unique=True, nullable=False);
    
    def __init__(self):
        self.card_type_id = None;
        self.card_type_name = None;
    
    def initData(self):
        self.data = CardTypes();
        self.data.description = 'lan on board';
        self.data.save();
        
        self.data = CardTypes();
        self.data.description = 'lan card';
        self.data.save();
        
        self.data = CardTypes();
        self.data.description = 'wireless';
        self.data.save();
        
        self.data = CardTypes();
        self.data.description = 'wireless on usb';
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
    
class Computers(DeclarativeBase):
    __tablename__ = 'computers';
    computers_id = Column(Integer, autoincrement=True, primary_key=True);
    computer_name = Column(String(255), unique=True, nullable=False);
    risk_section_id = Column(   Integer,ForeignKey('risk_section.risk_section_id'), nullable=False, index=True) ;
    risk_section = relation('RiskSection', backref='computer');
    
    computer_types_id= Column(   Integer,ForeignKey('computer_types.computer_types_id'), nullable=False, index=True) ;
    computer_types = relation('ComputerTypes', backref='computer');
    
    description  = Column(String(255), unique=True, nullable=False);
    location  = Column(String(255), unique=True, nullable=False);
    active  =  Column(String(1) , nullable=False,default =1);
    
    
    def __init__(self):
        self.computers_id = None;
        self.computer_name = None;
        self.risk_section_id = 0;        
        self.computer_types_id = 0;        
        self.description = None;
        self.location = None;
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
        return DBSession.query(cls) .get(str(id)); 

class ComputerIPMac(DeclarativeBase):
    __tablename__ = 'computer_ip_mac'  ;
    computer_ip_mac_id = Column(Integer, autoincrement=True, primary_key=True);
    
    computers_id = Column(   Integer,ForeignKey('computers.computers_id'), nullable=False, index=True) ;
    computers_name = relation('Computers', backref='computerip');
    
    card_types_id = Column(   Integer,ForeignKey('card_types.card_types_id'), nullable=False, index=True) ;
    card_types = relation('CardTypes', backref='computerip');
    
    computers_ip = Column(String(255), unique=True, nullable=False);
    computer_mac = Column(String(255), unique=True, nullable=False);
    
    active  =  Column(String(1) , nullable=False,default =1);
    
    def __init__(self):
        self.computer_ip_mac_id = None;
        
        self.computers_id = 0;        
        self.card_types_id = 0;        
        
        self.computers_ip = None;
        self.computer_mac = None;
         
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
        return DBSession.query(cls) .get(str(id));  
     