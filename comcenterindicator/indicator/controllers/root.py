# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController
from tg import expose, flash, require, url, lurl, request, redirect, validate, session, response
from tg.i18n import set_lang,get_lang, ugettext as _
from tgext.pluggable import app_model
#from indicator import model
#from indicator.model import DBSession
from comcenter.controllers.util.utility import Utility
from comcenter.controllers.util.exportexcel.risktoexcel import RiskToExcel
from datetime import datetime,date,time,timedelta;
from json import loads;

import logging;
import sys;
log = logging.getLogger(__name__);

class RootController(TGController):
    
    def __init__(self):
        self.util = Utility();
        
    @expose('indicator.templates.indicator.index')
    def index(self):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        set_lang("th"); 
        session['lang'] = "th";
        session.save();
        
        sectionid ="";
        userid = "";
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
            redirect('/indicator/add');
        
        log.info("indicator");
        
        dates = datetime.now();
        dyear = dates.strftime("%Y");
        dmonth = dates.strftime("%m");
        
        year =str( int(dyear) + 543  );
        month =  str(dmonth);  
        
        
        return dict(page='indicator',user=str(userid),sectionid=str(sectionid),level=level,year = year,month = month);
        
    @expose('indicator.templates.indicator.add')
    def add(self):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        set_lang("th"); 
        session['lang'] = "th";
        session.save();
        
        sectionid ="";
        userid = "";
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
            redirect('/indicator/');
        
        log.info("indicator");
        
        dates = datetime.now();
        dyear = dates.strftime("%Y");
        dmonth = dates.strftime("%m");

        #if(dmonth >= 10):
        #    dyear = int(dyear) + 1;

        
        year =str( int(dyear) + 543  );
        month =  str(dmonth);  
        #log.info("year : " + str(year) );
        #log.info("month : " + str(month) );
        return dict(page='indicator',user=str(userid),sectionid=str(sectionid),level=level,year = year,month = month);
    
    def saveLogView(self):
        self.ip=request.environ.get("X_FORWARDED_FOR", request.environ["REMOTE_ADDR"]);
        self.userid ='';
        if request.identity:
            self.userid = request.identity['repoze.who.userid'];
        self.logview = app_model.LogviewReport();
        self.logview.saveLogview(str(self.userid),str(self.ip),'2'  );
        
    @expose('indicator.templates.indicator.report1')
    def report1(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        set_lang("th");
        session['lang'] = "th";
        session.save();
        
        year = self.util.isValue(kw.get('year'));
        print "year : %s" %year 
        self.team_id =  self.util.numValue( kw.get('team_id')) ; 
        
        log.info( "team id " + str(self.team_id) );
        
        disabledSelect = False;
        level = "1";
        userid = None;
        sectionTeamId = 0;
        sectionid = 0;
        if request.identity:
            userid = request.identity['repoze.who.userid'];
            section = app_model.UserRiskSection.getByUserName(userid);
            if(section):
                sectionid = section.risk_section_id;
                
                self.team_id =   sectionid;
               
                disabledSelect = True;
        else:
            userid = None;       
      
        log.info( "team id " + str(self.team_id) ); 
       
        
         
        if year is None:
            year = 2558;
            
        listYear = self.util.getRangeYear(year);
        
        self.teamName ="";
        
        self.listTeam = app_model.RiskSection.listAll();
        self.listTeamCrom = [];
        for temp in self.listTeam:
            if( int(self.team_id) == int(temp.risk_section_id)    ):
                self.teamName = temp.description;
                self.listTeamCrom.append( { "risk_team_id" : temp.risk_section_id ,  "description"  :temp.description , "selected" : True });
            else:
                self.listTeamCrom.append( { "risk_team_id" : temp.risk_section_id ,  "description"  :temp.description , "selected" : False });
       
       
        listHash =  app_model.IndicatorsService.listReport1Indicator(self.team_id,year);
       
        #log_view_report
        self.saveLogView();
         
        return dict(page='indicator',listteam = self.listTeamCrom,util=self.util,year=year ,listYear = listYear,teamName = self.teamName,disabledSelect =disabledSelect ,listHash=listHash  );   
        #return dict(page='risk',util=self.util,year=year,month=month,listMonth=listMonth,listYear = listYear,section=section,pro_clinic=pro_clinic ,pro_physic=pro_physic,priority10=priority10,priority10inphysic = priority10InPhysic,startDate = startDate,stopDate= stopDate);
    
      
        
    @expose('indicator.templates.indicator.report2')
    def report2(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        set_lang("th");
        session['lang'] = "th";
        session.save();
        
        year = self.util.isValue(kw.get('year'));
        disabledSelect = False;
        sectionTeamId = 0;
        log.info(year);
        if year is None:
            year = 2558;
            
        listYear =self.util.getRangeYear(year);
       
        listHash =app_model.IndicatorsService.listReport2Indicator(year);
       
        #log_view_report
        self.saveLogView();
         
        return dict(page='indicator',year=year ,listYear = listYear,  listHash=listHash  );   
        #return dict(page='risk',util=self.util,year=year,month=month,listMonth=listMonth,listYear = listYear,section=section,pro_clinic=pro_clinic ,pro_physic=pro_physic,priority10=priority10,priority10inphysic = priority10InPhysic,startDate = startDate,stopDate= stopDate);
        
    @expose('json')
    def updateIndicator(self, **kw):
        #print kw;
         
        df = loads(request.body, encoding=request.charset);
         
        data = df['root'];
        
        years_id = session.get('years_id');
        months_id = session.get('months_id');
        
        for value in data:
            print value['indicator_value'];
            #years_id =  value['years_id'];
            #months_id  =  value['months_id'];      
            indicators_service = str(self.util.valueNull ( value['indicators_service_id']  ) );
            indicators_detail_id = value['indicators_detail_id'];
            risk_section_id = value['risk_section_id'];
            indicator_value = value['indicator_value'];
            years_id= value['years_id'];
            
            if(len(indicators_service) ==0):
                indicatorsService = app_model.IndicatorsService();
                indicatorsService.indicators_detail_id = indicators_detail_id;
                indicatorsService.years_id = years_id;
                indicatorsService.months_id = months_id;
                indicatorsService.risk_section_id = risk_section_id;
                indicatorsService.indicator_value = indicator_value;
                log.info("save service indicators:");
                indicatorsService.save();
            else:
                indicatorsService = app_model.IndicatorsService.getById(indicators_service);
                indicatorsService.indicator_value = indicator_value;
                log.info("update service indicators:");
                
                
                
                
        #print request.POST['root'].getall();
        #print request.GET.get['indicator_value'];
        return dict(success= True,message="update success");
        
    
    @expose()
    def updateIndicator1(self, **kw):
        print kw;
        
        #print request.headers;
        #print request.body ;
        #print request.GET.get['indicator_value'];
        #return dict(success= True,message="update success");
        
        response.headers['Content-type'] = "application/json";
        
        return {"success" : True,'message':"update success"};
        
        
    @expose('json')
    def listIndicatorBySection(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        set_lang("th"); 
        session['lang'] = "th";
        session.save();
        
        sectionid = self.util.isValue(kw.get('riskSection'));
        years_id = self.util.isValue(kw.get('year'));
        months_id = self.util.isValue(kw.get('month'));
        start_year = self.util.isValue(kw.get('year'));
        
        print sectionid;
        print years_id;
        print months_id;
        
        
        dates = datetime.now();
        dyear = dates.strftime("%Y");
        dmonth = dates.strftime("%m");
        
        if(years_id is None):
            years_id =str( int(dyear) + 543  );
       
        if (months_id is None):
            months_id = str(dmonth);
       
        
        session['months_id'] = months_id;
        session['years_id'] = years_id;
        session.save();
        
        #sectionid = 2;
        #years_id = 2556;
        #months_id = 11;
        
        #if ( int(months_id) >9 ) :
         #   #years_id = int(years_id) + 1;
        #    years_id = int(years_id) - 1;
        
        #log.info(str(years_id));
        
        self.List = app_model.IndicatorsService.listIndicatorBySection(sectionid , years_id,start_year, months_id);
        
        return dict(root = self.List,total=str(len(self.List)));
        
    @expose('json')
    def listSection(self ,**kw):
        section_id = self.util.isValue(kw.get('section_id'));
        self.list = [];
        if(section_id is None):
            self.listType = app_model.RiskSection.listAll();
            self.list.append({'id':'0','name':'*'});
             
        else:
            self.listType = app_model.RiskSection.listBySection(section_id);
        
        if(self.listType):
                for value in self.listType:
                    self.list.append({'id':value.risk_section_id,'name':value.description}); 
                        
        return dict(root = self.list,total=str(len(self.list)));
    
    
    
    @expose('json')
    def listMonths(self ,**kw):
        log.info("list month");
        self.listValue = app_model.Months.listAll();
        self.List = [];
         
        if(self.listValue):
            for value in self.listValue:
                self.List.append({'id':value.months_id,'name':value.month  }); 
        return dict(root = self.List,total=str(len(self.List)));
    
    @expose('json')
    def listYears(self ,**kw):
         
        self.listValue = app_model.Years.listAll();
        self.List = [];
         
       # self.List.append({'id':'0','name':'*'});
        if(self.listValue):
            for value in self.listValue:
                self.List.append({'id':value.years_id,'name':value.year  }); 
        return dict(root = self.List,total=str(len(self.List)));
