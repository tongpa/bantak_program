# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController
from tg import expose, flash, require, url, lurl, request, redirect, validate, session, response
from tg.i18n import set_lang,get_lang, ugettext as _
from tgext.pluggable import app_model

from comcenter.controllers.util.utility import Utility
from comcenter.controllers.util.exportexcel.projecttoexcel import ProjectToExcel;
from datetime import datetime,date,time,timedelta;
from json import loads;

import logging;
import sys;
log = logging.getLogger(__name__);

class RootController(TGController):
    
    def __init__(self):
        self.util = Utility();
        
    @expose('computer.templates.computer.index')
    def index(self):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        print "Index maintenance";
        """Handle the front-page."""
        set_lang("th"); 
        session['lang'] = "th";
        session.save();
        userid = "";
        sectionid ="";
        level = "1"; #Admin;  0 user;
        if request.identity:
            userid = request.identity['repoze.who.userid'];
            
            section = app_model.UserRiskSection.getByUserName(userid);
            if(section):
                sectionid = section.risk_section_id;
                section = app_model.RiskSection.listBySectionbyId(sectionid);
                if(section):
                    userid = section.description;
                    level = "0";
                
            print "section : " + str(sectionid);
        else:
            #redirect('/computer/add');
            pass;
        
        log.info("computer");
        #print "user : " + str(userid);
             
            
        return dict(page='computer',user=str(userid),sectionid=str(sectionid),level=level);
    
    
    @expose('json')
    def listComputerTypes(self ,**kw):
         
         
        self.listLevel = app_model.ComputerTypes.listAll();
        
         
        self.listDataRiskLevel = [];
       # self.listDataRiskLevel.append({'id':'0','name':'*'});
        if(self.listLevel):
            for value in self.listLevel:
                self.listDataRiskLevel.append({'id':value.computer_types_id,'name':value.description  }); 
        return dict(root = self.listDataRiskLevel,total=str(len(self.listDataRiskLevel)));
    
    @expose('json')
    def listCardType(self,**kw):
        self.listLevel = app_model.CardTypes.listAll();
        
         
        self.listDataRiskLevel = [];
       # self.listDataRiskLevel.append({'id':'0','name':'*'});
        if(self.listLevel):
            for value in self.listLevel:
                self.listDataRiskLevel.append({'id':value.card_types_id,'name':value.description  }); 
        return dict(root = self.listDataRiskLevel,total=str(len(self.listDataRiskLevel)));
    
    
    @expose('json')
    def saveComputer(self,**kw):
        
        
        computers_id =self.util.isValue( kw.get('computers_id') ) ;
        computer_name = self.util.isValue(kw.get('computer_name'));
        risk_section_id =self.util.isValue( kw.get('risk_section_id') );       
        
        computer_types_id=self.util.isValue( kw.get('computer_types_id'));
        
        
        description  = self.util.isValue(kw.get('description'));
        location  =self.util.isValue( kw.get('location'));
        active  =self.util.isValue( kw.get('active'));
        
        
        return dict(root='');