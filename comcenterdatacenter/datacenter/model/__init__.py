# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from tgext.pluggable import PluggableSession

DBSession = PluggableSession()
DeclarativeBase = declarative_base()

def init_model(app_session):
    DBSession.configure(app_session)


from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime
from sqlalchemy.orm import backref, relation
from tgext.pluggable import app_model, primary_key

class Sample1(DeclarativeBase):
    __tablename__ = 'plugdatacenter_samples'

    uid = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode(16))

    #uid_indicator = Column(Integer, ForeignKey(primary_key(app_model.Sample)))
    #indicator = relation(app_model.Sample)