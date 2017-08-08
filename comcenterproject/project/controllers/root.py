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
        self.projectToExcel = ProjectToExcel();
        
    @expose('project.templates.project.index')
    def index(self):
        print "Index maintenance";
        """Handle the front-page."""
        set_lang("th"); 
        session['lang'] = "th";
        session.save();
        userid = "";
        if request.identity:
            userid = request.identity['repoze.who.userid']
        else:
            redirect('/project/summary');
        
        log.info("project");
            #print "user : " + str(userid);
        return dict(page='project')
    
    @expose('project.templates.project.summary')
    def summary(self):
        print "Index maintenance";
        """Handle the front-page."""
        set_lang("th"); 
        session['lang'] = "th";
        session.save();
        userid = "";
        if request.identity:
            userid = request.identity['repoze.who.userid']
            #print "user : " + str(userid);
        return dict(page='project_summary')
    
    
    
    @expose('json')
    def listSection(self ,**kw):
        
        divisionId = self.util.isValue(kw.get('division'));
        self.listType = [];
        if(divisionId):
            self.listType = app_model.Section.listByDivision(divisionId);
        else:
            self.listType = app_model.Section.listAll();
        self.list = [];
        self.list.append({'id':'0','name':'*'});
        if(self.listType):
            for value in self.listType:
                self.list.append({'id':value.section_id,'name':value.description}); 
        return dict(root = self.list,total=str(len(self.list)));
    @expose('json')
    def listStatus(self ,**kw):
        
        self.listType = app_model.ProjectStatus.listAll();
        self.list = [];
        self.list.append({'id':'0','name':'*'});
        if(self.listType):
            for value in self.listType:
                self.list.append({'id':value.project_status_id,'name':value.project_status_name}); 
        return dict(root = self.list,total=str(len(self.list)));
    
    @expose()
    def example(self,**kw):
        
        app_model.Project.querySummary();
    
  
  
    @expose('json')
    def showGraphByDivision(self,**kw):
        fiscalyear = self.util.isValue( kw.get('fiscalyear') ) ;
        division = self.util.isValue( kw.get('division') ) ;
        section = self.util.isValue( kw.get('section') ) ;
        status = self.util.isValue( kw.get('status') ) ;
        projectType =  self.util.isValue( kw.get('projectType') ) ;
        
        self.listType = app_model.Project.querySummary( fiscalyear, division, section,status,projectType);
         
        return dict(root = self.listType,total=str(len(self.listType)));
    
    @expose('json')
    def listProject(self ,**kw):
        
        # print kw;
        
        fiscalyear = self.util.isValue( kw.get('fiscalyear') ) ;
        division = self.util.isValue( kw.get('division') ) ;
        section = self.util.isValue( kw.get('section') ) ;
        status = self.util.isValue( kw.get('status') ) ;
        projectType =  self.util.isValue( kw.get('projectType') ) ;
        
        self.listType = app_model.Project.search( fiscalyear, division, section,status,projectType);
        self.list = [];
        #self.list.append({'id':'0','name':'*'});
        if(self.listType):
            for value in self.listType:
                allBudget = value.budget + value.budget_other + value.maintenance_funds_budget;
                self.list.append({'project_id':value.project_id,'project_name':value.project_name,
                                  'project_budget':value.budget,'user_name':value.owner,
                                  'project_status':value.project_status.project_status_name,
                                  'department': value.department.description,
                                  'division':value.division.description,
                                  'section':value.section.description,
                                  'project_type':value.project_type.project_type_name,
                                  'projectType':value.project_type.project_type_id,
                                  'division_id':value.division.division_id,
                                  'section_id':value.section.section_id,
                                  'detail':value.detail,
                                  'start_date':value.start_date,
                                  'stop_date':value.stop_date,
                                  'project_status_id':value.project_status.project_status_id,
                                  'fiscal_year' : value.fiscal_year,
                                  'budget_other':value.budget_other,
                                  'budget_other_from':value.budget_other_from,
                                  'maintenance_funds_budget':value.maintenance_funds_budget,
                                  'plantype_id' : value.plantype_id,
                                  'plantype' : value.plantype.plantype_name,
                                  'allBudget' :allBudget
                                   }); 
                                   
       # self.projectToExcel.exportToExcel(self.list);
        
        return dict(root = self.list,total=str(len(self.list)));
    
    
    @expose(content_type="application/ms-excel")
    def ExportProjectToExcel(self ,**kw):
        
       # print kw;
        
        fiscalyear = self.util.isValue( kw.get('fiscalyear') ) ;
        division = self.util.isValue( kw.get('division') ) ;
        section = self.util.isValue( kw.get('section') ) ;
        status = self.util.isValue( kw.get('status') ) ;
        projectType =  self.util.isValue( kw.get('projectType') ) ;
        
        self.listType = app_model.Project.search( fiscalyear, division, section,status,projectType);
        self.list = [];
        #self.list.append({'id':'0','name':'*'});
        if(self.listType):
            for value in self.listType:
                allBudget = value.budget + value.budget_other + value.maintenance_funds_budget;
                self.list.append({'project_id':value.project_id,'project_name':value.project_name,
                                  'project_budget':value.budget,'user_name':value.owner,
                                  'project_status':value.project_status.project_status_name,
                                  'department': value.department.description,
                                  'division':value.division.description,
                                  'section':value.section.description,
                                  'project_type':value.project_type.project_type_name,
                                  'projectType':value.project_type.project_type_id,
                                  'division_id':value.division.division_id,
                                  'section_id':value.section.section_id,
                                  'detail':value.detail,
                                  'start_date':value.start_date,
                                  'stop_date':value.stop_date,
                                  'project_status_id':value.project_status.project_status_id,
                                  'fiscal_year' : value.fiscal_year,
                                  'budget_other':value.budget_other,
                                  'budget_other_from':value.budget_other_from,
                                  'maintenance_funds_budget':value.maintenance_funds_budget,
                                  'plantype_id' : value.plantype_id,
                                  'plantype' : value.plantype.plantype_name,
                                  'allBudget' :allBudget
                                   }); 
                                   
        pathfile = self.projectToExcel.exportToExcel(self.list);
        
        print pathfile;
        response.content_type = 'application/ms-excel'
        response.headers["Content-Disposition"] = "attachment;filename=project.xls"
         
        file = open(pathfile,'rb');
        read_data = file.read();
      
        return read_data;
    
    #    return dict(root = self.list,total=str(len(self.list)));
    
    @expose('json')
    def listProjectType(self ,**kw):
        
        self.listType = app_model.ProjectType.listAll();
        self.list = [];
        self.list.append({'id':'0','name':'*'});
        if(self.listType):
            for value in self.listType:
                self.list.append({'id':value.project_type_id,'name':value.project_type_name}); 
        return dict(root = self.list,total=str(len(self.list)));
    
    @expose('json')
    def deleteProject(self,**kw):
        print "deleteProject";
        #print kw;
        self.success = True;
        self.message ="success";
        
        projectId = self.util.isValue(kw.get('project_id'));
        
        try:
            if(projectId):
                self.project = app_model.Project.getById(projectId);
                if(self.project):
                    self.project.remove();
                else:
                    log.info("error : remove : "+ str(projectId) );
                    self.message ="fail";
                    self.success = False;
            else :
                log.info("error : remove : "+ str(projectId) );
                self.message ="fail";
                self.success = False;
        except Exception, exception:
            log.info("error : " + str(exception));
            self.message ="fail";
            self.success = False;
        
        return dict(success=self.success, message = self.message); 
    @expose('json')
    def createProject(self, **kw):
        print "createProject";
        
        #print kw;
        
        #print  kw.get('project_name');
        projectId = self.util.isValue(kw.get('project_id'));
        
        
        self.message ="success";
        self.success =True;
        try:
            if(projectId):
                log.info("update value");
                self.project = app_model.Project.getById(projectId);
                 
                self.project.project_type_id = kw.get('projectType');
                self.project.project_name = kw.get('project_name');
                self.project.budget = kw.get('project_budget');
                self.project.division_id = kw.get('division_id');
                self.project.section_id = kw.get('section_id');
                self.project.detail = kw.get('detail');
                self.project.owner = kw.get('user_name');
                self.project.fiscal_year = kw.get('fiscal_year');
                self.project.budget_other = kw.get('budget_other');
                self.project.budget_other_from = kw.get('budget_other_from');
                self.project.maintenance_funds_budget = kw.get('maintenance_funds_budget');
                self.project.plantype_id = self.util.isValue(kw.get('planType'));
                
                self.project.department_id = 1;
                 
                
                self.project.start_date = self.util.convertStringToDate(kw.get('start_date'));
                self.project.stop_date = self.util.convertStringToDate(kw.get('stop_date'));
                
                self.project.project_status_id = kw.get('project_status_id');
                #self.project.update();
            else:
                log.info("save value"); 
                
                self.project =  app_model.Project();
                self.project.project_type_id = kw.get('projectType');
                self.project.project_name = kw.get('project_name');
                self.project.budget = kw.get('project_budget');
                self.project.division_id = kw.get('division_id');
                self.project.section_id = kw.get('section_id');
                self.project.detail = kw.get('detail');
                self.project.owner = kw.get('user_name');
                self.project.fiscal_year = kw.get('fiscal_year');
                self.project.budget_other = kw.get('budget_other');
                self.project.budget_other_from = kw.get('budget_other_from');
                self.project.maintenance_funds_budget = kw.get('maintenance_funds_budget');
                self.project.plantype_id = self.util.isValue(kw.get('planType'));
                
                self.project.department_id = 1;
                 
                
                self.project.start_date = self.util.convertStringToDate(kw.get('start_date'));
                self.project.stop_date = self.util.convertStringToDate(kw.get('stop_date'));
                
                self.project.project_status_id = 1;
                
                self.project.save();
        except Exception, exception:
            log.info("error : " + str(exception));
            self.message ="fail";
            self.success = False;
                
        return dict(success=self.success, message = self.message);
    
    
    @expose('json')
    def getCalendar(self, **kw):
        self.list = [];
        self.list.append({"id":1001,"cid":1,"start":"2011-08-06T10:00:00+08:00","end":"2011-08-16T15:00:00+08:00","title":"Vacation","notes":"Have fun"});
        self.list.append({"id":1002,"cid":2,"start":"2011-08-26T11:30:00+08:00","end":"2011-08-26T13:00:00+08:00","title":"Lunch with Matt","loc":"Chuy's","url":"http:\/\/chuys.com","notes":"Order the queso"});
        self.list.append({"id":1003,"cid":3,"start":"2011-08-26T15:00:00+08:00","end":"2011-08-26T15:00:00+08:00","title":"Project due"});
        self.list.append({"id":1004,"cid":1,"start":"2011-08-26T00:00:00+08:00","end":"2011-08-26T00:00:00+08:00","title":"Sarah's birthday","ad":True,"notes":"Need to get a gift"});
        
        return dict (success=True,message="Loaded Data",data = self.list);
