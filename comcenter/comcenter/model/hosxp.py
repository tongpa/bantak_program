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
from sqlalchemy.types import Unicode, Integer, DateTime
from sqlalchemy.orm import relation, synonym
from sqlalchemy import *;

from comcenter.model import DeclarativeBase2, metadata2, DBSession2
#from sqlalchemy.sql.expression import *;
import logging;
import sys;
log = logging.getLogger(__name__);

#__all__ = ['User', 'Group', 'Permission']

class VisitTransection(object):
    def __init__(self):
        pass;
    @classmethod
    def queryVisitInYear(cls,year=None):
        sql = text("""select
                        vn_stat.ym ,
                        count(vn_stat.vn) as count_vn
                    from 
                        vn_stat
                    where vn_stat.ym like :year
                    group by vn_stat.ym """, bindparams=[ bindparam('year', str(year+'%')) ]);
         
        result = DBSession2.execute(sql );
        return result ; 
    
    @classmethod
    def queryPatientInYear(cls,year=None):
        """select
                        pt.ym,
                        count(pt.hn) as count_hn
                      from (
                          select
                              vn_stat.ym,
                              vn_stat.hn
                          from vn_stat
                          where vn_stat.ym like :year
                          group by
                              vn_stat.hn
                      ) as pt
                      group by pt.ym """
                      
        sql = text("""select
                            vn_stat.ym,
                            count( distinct vn_stat.hn ) as count_hn
                      from vn_stat
                      where vn_stat.ym like :year
                      group by vn_stat.ym""", bindparams=[ bindparam('year', str(year+'%')) ]);
         
        result = DBSession2.execute(sql );
        return result ;
    
    @classmethod
    def queryPatientSexInYear(cls,year=None):
        sql = text(""" select
                            pt.ym,
                            sum(pt.men) as men ,
                            sum(pt.women) as women 
                       from (
                               select
                                   vn_stat.ym,
                                   case when vn_stat.sex = 1 then 1 else 0 end as men,
                                   case when vn_stat.sex = 2 then 1 else 0 end as women
                               from vn_stat
                               where vn_stat.ym like :year
                               group by vn_stat.ym,vn_stat.hn
                        ) pt
                        group by pt.ym """, bindparams=[ bindparam('year', str(year+'%')) ]);
         
        result = DBSession2.execute(sql );
        return result ; 
