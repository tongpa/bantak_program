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
        
    @expose('maintenance.templates.maintain.index')
    def index(self):
        print "Index maintenance";
        """Handle the front-page."""
        set_lang("th"); 
        session['lang'] = "th";
        session.save();
        userid = "";
        if request.identity:
            userid = request.identity['repoze.who.userid']
            print "user : " + str(userid);
        return dict(page='index')
    
    @expose()
    def createMaintain(self, **kw):
        print kw;
        
        pass;
    
    @expose('json')
    def listDivision(self ,**kw):
        
        self.listType = app_model.Division.listAll();
        self.list = [];
        self.list.append({'id':'0','name':'*'});
        if(self.listType):
            for value in self.listType:
                self.list.append({'id':value.division_id,'name':value.description}); 
        return dict(root = self.list,total=str(len(self.list)));
    
    @expose('json')
    def listMaintenaceType(self ,**kw):
        
        self.listType = app_model.MaintenanceType.listAll();
        self.list = [];
        self.list.append({'id':'0','name':'*'});
        if(self.listType):
            for value in self.listType:
                self.list.append({'id':value.mtn_type_id,'name':value.description}); 
        return dict(root = self.list,total=str(len(self.list)));
    
