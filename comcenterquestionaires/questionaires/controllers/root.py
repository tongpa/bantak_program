# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController
from tg import expose, flash, require, url, lurl, request, redirect, validate, session, response
from tg.i18n import set_lang,get_lang, ugettext as _
from tgext.pluggable import app_model

from comcenter.controllers.util.utility import Utility

from datetime import datetime,date,time,timedelta;
from json import loads;

import logging;
import sys;
log = logging.getLogger(__name__);

class RootController(TGController):
    
    def __init__(self):
        self.util = Utility();
        self.defaultyear = 2557;
        
    @expose('questionaires.templates.risk.questionaires')
    def index(self):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        print "Index maintenance";
        """Handle the front-page."""
              
            
        return dict(page='risk');
    
    @expose('questionaires.templates.risk.questgroup')
    def qgroup(self):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        print "Index maintenance";
        """Handle the front-page."""
              
            
        return dict(page='risk');
    
    @expose('json')
    def queryBySumLevelBy(self ,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        """Handle the front-page."""
        print "queryBySumLevelBy";
        col1= kw.get("column1");
        col2= kw.get("column2");
        print col2;
        
        list = [];
        list = app_model.Questionnaires.queryBySumLevelBy(column1=col1,column2=col2);
        print "size : " + str(len(list));
        return dict(root = list,total=str(len(list)));
       
    
    @expose('json')
    def queryByAvgBy(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        
        print "queryByAvgBy";
        col1 = kw.get("column1");
        col2 = kw.get("column2");
        
        list = [];
        list = app_model.Questionnaires.queryByAvgBy(column1 = col1 , column2= col2);
        print "size : " + str(len(list));
        return dict(root = list,total=str(len(list)));
    
    @expose('json')
    def queryByMedianGroup(self ,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        """Handle the front-page."""
        print "queryBySumLevelBy";
        list = [];
        list = app_model.Questionnaires.queryByMedianGroup(group=1);
        print "size : " + str(len(list));
        return dict(root = list,total=str(len(list)));
