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

__all__ = ['ReservationRoom', 'Reservation']

class ReservationRoom(DeclarativeBase):
    __tablename__ = 'reservation_room';
    reservation_room_id = Column(Integer, autoincrement=True, primary_key=True);
    room_name = Column(String(255), unique=True, nullable=False);
    
    def __init__(self):
        self.reservation_room_id = None;
        self.room_name = None;
        
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

class Reservation(DeclarativeBase):
    __tablename__ = 'reservation';
    reservation_id = Column(Integer, autoincrement=True, primary_key=True);
    reservation_room_id = Column(   Integer,ForeignKey('reservation_room.reservation_room_id'), nullable=False, index=True) ;
    reservation_room = relation('ReservationRoom', backref='reservation');
    book_name =   Column(String(255), nullable=False);
    detail  = Column(   Text, nullable=False);
    division_id = Column(   Integer,ForeignKey('division.division_id'), nullable=False, index=True) ;
    division  = relation('Division', backref='reservation');
    section_id = Column(   Integer,ForeignKey('section.section_id'), nullable=False, index=True) ;
    section  = relation('Section', backref='reservation');
    start_date_time  = Column(DateTime, nullable=False, default=datetime.now);
    stop_date_time  = Column(DateTime, nullable=True);
    create_date =  Column(DateTime, nullable=False, default=datetime.now);
    active =   Column(Integer, default=1 );
    
    
    def __init__(self):
        self.reservation_id = None;
        self.reservation_room_id = None;
        self.reservation_room = None;
        self.book_name = None;
        self.detail = None;
        self.division_id = 0;
        self.section_id = 0;
        self.start_date_time = None;
        self.stop_date_time = None;
        self.create_date =  datetime.now();
        self.active = 1;
        
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