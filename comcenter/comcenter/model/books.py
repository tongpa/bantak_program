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

from sqlalchemy import Table, ForeignKey, Column, between, and_, or_
from sqlalchemy.types import Unicode, Integer, DateTime, String, Text
from sqlalchemy.orm import relation, synonym
from sqlalchemy import *;
from comcenter.model import DeclarativeBase, metadata, DBSession
#from sqlalchemy.sql.expression import *;
import logging;
import sys;
log = logging.getLogger(__name__);

__all__ = ['BookType', 'Book' ,'BookFile']

class BookType(DeclarativeBase):
    __tablename__ = 'book_type';
    book_type_id = Column(Integer, autoincrement=True, primary_key=True);
    book_type_name = Column(String(255), unique=True, nullable=False);
    
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
    
    @classmethod
    def listAll(cls):
        return DBSession.query(cls).order_by(cls.book_type_id).all(); 
        
    def initData(self):
        self.data = BookType();
        
        #self.data.book_type_id = 1;
        self.data.book_type_name = 'ทะเบียนหนังสือรับภายใน';
        self.data.save();
        
        #self.data.book_type_id = 2;
        self.data.book_type_name = 'ทะเบียนหนังสือรับภายนอก';
        self.data.save();
        
        #self.data.book_type_id = 3;
        self.data.book_type_name = 'ทะเบียนหนังสือส่งภายใน';
        self.data.save();
        
        #self.data.book_type_id = 4;
        self.data.book_type_name = 'ทะเบียนหนังสือส่งภายนอก';
        self.data.save();

class BookFile(DeclarativeBase):
    __tablename__ = 'book_file'
    book_file_id =   Column(Integer, autoincrement=True, primary_key=True);
    book_id = Column(   Integer,ForeignKey('book.book_id'), nullable=False, index=True) ; 
    orig_file_name =  Column(String(255),    nullable=False);
    new_file_name =  Column(String(255),    nullable=False);
    create_date  =  Column(DateTime, nullable=False, default=datetime.now);
    def __init__(self):
        self.book_file_id = None;
        self.book_id = None;
        self.orig_file_name = None;
        self.new_file_name = None;
        self.create_date  =  datetime.now(); 
        
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
        return DBSession.query(cls).get(id);   
    
    @classmethod
    def getByBookId(cls,id):
        return DBSession.query(cls).filter(cls.book_id == id).all();   
    
class Book(DeclarativeBase):
    
    __tablename__ = 'book' 
    book_id =  Column(Integer, autoincrement=True, primary_key=True);
    book_number =  Column(String(255), index=True,  nullable=False);
    book_at  =  Column(String(255), index=True,  nullable=False);
    book_recive  =  Column(DateTime, nullable=False, default=datetime.now);
    book_from  =  Column(String(255), index=True,  nullable=True);
    book_to  =  Column(String(255), index=True,  nullable=True);
    book_detail  =  Column(   Text, nullable=True);
    book_operations  =  Column(   Text, nullable=True);
    book_remark  =  Column(   Text, nullable=True);
    create_date  =  Column(DateTime, nullable=False, default=datetime.now);
    update_date  =  Column(DateTime, nullable=True);
    activate  =   Column(String(2), index=True,  nullable=False , default= 0);
    book_type_id = Column(   Integer,ForeignKey('book_type.book_type_id'), nullable=False, index=True) ; 
    book_type  = relation('BookType', backref='book');
     
    def __init__(self):
        self.book_id = None;
        self.book_number = None;
        self.book_at = None;
        self.book_recive =  datetime.now();
        self.book_from = None;
        self.book_to = None;
        self.book_detail = None;
        self.book_operations = None;
        self.book_remark = None;
        self.create_date=  datetime.now();
        self.update_date = None;
        self.activate = '1';
        self.book_type_id = 0;
        
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
        return DBSession.query(cls).get(id);      
    
    @classmethod
    def showProgramClinicReport(cls,startDate, stopDate,book_type,bookSearch,offset=0,limit=15):
        
        query = DBSession.query(cls).filter( and_( cls.activate == '1', and_( cls.book_detail.like(bookSearch) ,and_( cls.book_type_id == book_type ,cls.book_recive.between(startDate, stopDate)  ) )) );
        count = query.count();
        list = query.order_by(desc(cls.book_number)).limit(limit).offset(offset).all();
        #DBSession.query(cls).filter(between(cls.book_recive, startDate, stopDate)).all();
        print count ;
        
        return count, list;   
    
    