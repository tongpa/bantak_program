# -*- coding: utf-8 -*-
"""The application's model objects"""

from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Global session manager: DBSession() returns the Thread-local
# session object appropriate for the current web request.
maker = sessionmaker(autoflush=True, autocommit=False,
                     extension=ZopeTransactionExtension())
DBSession = scoped_session(maker)

# Base class for all of our model classes: By default, the data model is
# defined with SQLAlchemy's declarative extension, but if you need more
# control, you can switch to the traditional method.
DeclarativeBase = declarative_base()

# There are two convenient ways for you to spare some typing.
# You can have a query property on all your model classes by doing this:
# DeclarativeBase.query = DBSession.query_property()
# Or you can use a session-aware mapper as it was used in TurboGears 1:
# DeclarativeBase = declarative_base(mapper=DBSession.mapper)

# Global metadata.
# The default metadata is the one from the declarative base.
metadata = DeclarativeBase.metadata

# If you have multiple databases with overlapping table names, you'll need a
# metadata for each database. Feel free to rename 'metadata2'.
# from sqlalchemy import MetaData
# metadata2 = MetaData()

#####
# Generally you will not want to define your table's mappers, and data objects
# here in __init__ but will want to create modules them in the model directory
# and import them at the bottom of this file.
######

maker2 = sessionmaker(autoflush=True, autocommit=False,
                     extension=ZopeTransactionExtension())
DBSession2 = scoped_session(maker2)
DeclarativeBase2 = declarative_base()
metadata2 = DeclarativeBase2.metadata

def init_model(engine):
    """Call me before using any of the tables or classes in the model."""
    DBSession.configure(bind=engine)
    print "---- : call init_model"
    
def init_model_multi(engineOne,engineTwo):
    """Call me before using any of the tables or classes in the model."""
    DBSession.configure(bind=engineOne)
    DBSession2.configure(bind=engineTwo);

    metadata.bind = engineOne;
    metadata2.bind = engineTwo;
    print "---- : call init_model_multi"

    # If you are using reflection to introspect your database and create
    # table objects for you, your tables must be defined and mapped inside
    # the init_model function, so that the engine is available if you
    # use the model outside tg2, you need to make sure this is called before
    # you use the model.

    #
    # See the following example:
    #
    # global t_reflected
    # t_reflected = Table("Reflected", metadata,
    #                     autoload=True, autoload_with=engine)
    # mapper(Reflected, t_reflected)

# Import your model modules here.
from comcenter.model.auth import User, Group, Permission

__all__ = ('User', 'Group', 'Permission')
from comcenter.model.auth import User, Group, Permission
from comcenter.model.coredb import *;
from comcenter.model.maintain import *;
from comcenter.model.project import *;
from comcenter.model.reservation import *;
from comcenter.model.revenue import *;
from comcenter.model.dental import *;
from comcenter.model.hosxp import *;
from comcenter.model.risk import *;
from comcenter.model.expenses import *;
from comcenter.model.books import *;
from comcenter.model.indicator import *;
from comcenter.model.computers import *;
from comcenter.model.logviewreport import *;