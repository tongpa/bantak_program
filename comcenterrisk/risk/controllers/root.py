# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController
from tg import expose, flash, require, url, lurl, request, redirect, validate, session, response

from tg.i18n import ugettext as _, lazy_ugettext as l_, set_lang,get_lang
from tgext.pluggable import app_model
#from comcenter.model import  User, UserRiskSection,RiskManagement,LogviewReport,RiskSection, RiskTeam, TestSample
#from comcenter.model import SectionListTeam, RiskLevel, RiskTeamType, RiskProgramDetail, RiskProgramGroup, RiskStatus, RiskResponsible

from datetime import datetime

from comcenter.controllers.util.utility import Utility
from comcenter.controllers.util.exportexcel.risktoexcel import RiskToExcel

from .adminriskmanagecontroller import AdminRiskManageController
from risk.service.riskservice import RiskService
import logging;
import sys;
log = logging.getLogger(__name__);

class RootController(TGController):
    
    admin = AdminRiskManageController()
    
    def __init__(self):
        self.util = Utility();
        self.export = RiskToExcel();
        self.defaultyear = int(datetime.now().strftime("%Y")) + int(543)#2558;
        
        self.riskservice = RiskService()
    @expose('risk.templates.index')
    def index_old(self):
        return dict(success = True)
        
    @expose('risk.templates.risk.index')
    def index(self):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        #print "Index maintenance";
        """Handle the front-page."""
        set_lang("th"); 
        session['lang'] = "th";
        session.save();
        userid = "";
        sectionid ="";
        level = "1"; #Admin;  0 user;
        user_display ="";
        ip=request.environ.get("X_FORWARDED_FOR", request.environ["REMOTE_ADDR"]);
        #print ip;
        #self.selectall = app_model.TestSample.selectAll()
        #print 'leng : %s' %len(self.selectall)
        
        #for d in self.selectall:
        #    print "value : %s" %d.user_id
        
        if request.identity:
            userid = request.identity['repoze.who.userid'];
            user_login = app_model.User.by_user_name(userid);
            section = app_model.UserRiskSection.getByUserName(userid);
            if(section):
                sectionid = section.risk_section_id;
                #display =section.display_name;
                section = app_model.RiskSection.listBySectionbyId(sectionid);
                if(section):
                    userid = section.description;
                    level = "0";
                #else:
                #    userid = display;
            
            user_display = user_login.display_name;
            print "section : " + str(sectionid);
        else:
            redirect('/risk/add');
        
        log.info("risk");
        #print "user : " + str(userid);
        return dict(page='risk',user=str(userid),user_display= str(user_display),sectionid=str(sectionid),level=level);
    
    @expose('risk.templates.risk.add')
    def add(self):
        set_lang("th");
        session['lang'] = "th";
        session.save();
        log.info("risk");
        return dict(page='risk',user='',sectionid='',level=0);
    
    def saveLogView(self):
        self.ip=request.environ.get("X_FORWARDED_FOR", request.environ["REMOTE_ADDR"]);
        self.userid ='';
        if request.identity:
            self.userid = request.identity['repoze.who.userid'];
        self.logview =  app_model.LogviewReport();
        self.logview.saveLogview(str(self.userid),str(self.ip),'1'  );
        
    
    @expose('risk.templates.risk.report1')
    def report1(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        set_lang("th");
        session['lang'] = "th";
        session.save();
        
        year = self.util.isValue(kw.get('year'));
        
        month = self.util.isValue(kw.get('month'));
        
        log.info("risk");
        listMonth =[];
        listMonth.append({'id':'1','value':'มกราคม'});
        listMonth.append({'id':'2','value':'กุมภาพันธ์'});
        listMonth.append({'id':'3','value':'มีนาคม'});
        listMonth.append({'id':'4','value':'เมษายน'});
        listMonth.append({'id':'5','value':'พฤษภาคม'});
        listMonth.append({'id':'6','value':'มิถุนายน'});
        listMonth.append({'id':'7','value':'กรกฎาคม'});
        listMonth.append({'id':'8','value':'สิงหาคม'});
        listMonth.append({'id':'9','value':'กันยายน'});
        listMonth.append({'id':'10','value':'ตุลาคม'});
        listMonth.append({'id':'11','value':'พฤศจิกายน'});
        listMonth.append({'id':'12','value':'ธันวาคม'});
        
        log.info(year);
        if year is None:
            year = self.defaultyear;
            
        listYear = self.util.getRangeYear(year);
        
        section = None;
        pro_clinic = None;
        pro_physic = None;
        priority10 =None;
        priority10InPhysic = None;
        
        stopDate = None;
        startDate = None;
        
        if (month and year):

            date = '1/'+str(month)+'/'+str(int(year)-543);
            startDate = self.util.convertStringToDate(date);
            stopDate = self.util.last_day_of_month(startDate);
            
            startDate = startDate.strftime("%Y-%m-%d");
            stopDate = stopDate.strftime("%Y-%m-%d");
             
        
            section =  app_model.RiskManagement.showSumSectionReport(startDate,stopDate);
            pro_clinic =  app_model.RiskManagement.showProgramClinicReport(startDate,stopDate,1);
            pro_physic =  app_model.RiskManagement.showProgramClinicReport(startDate,stopDate,2);
            priority10 =  app_model.RiskManagement.listRiskPriority10(startDate,stopDate, 10);
            
            priority10InPhysic =  app_model.RiskManagement.listRiskPriority10Physic(startDate,stopDate, 10);
            
            #log_view_report
            self.saveLogView();
        

            
        return dict(page='risk',util=self.util,year=year,month=month,
                    listMonth=listMonth,listYear = listYear,section=section,
                    pro_clinic=pro_clinic ,pro_physic=pro_physic,priority10=priority10,
                    priority10inphysic = priority10InPhysic,startDate = startDate,stopDate= stopDate);
    
    @expose('risk.templates.risk.report2')
    def report2(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        set_lang("th");
        session['lang'] = "th";
        session.save();
        
        year = self.util.isValue(kw.get('year'));
        
        log.info(year);
        if year is None:
            year = self.defaultyear;
            
        listYear = self.util.getRangeYear(year);
                
        section=[];
        if(year):
            startDate = str(int(year)-543 -1) + '-10-01';
            stopDate = str(int(year)-543) + '-09-30';
            log.info(startDate);
            section =  app_model.RiskManagement.listSectionReport(startDate,stopDate);
            #log_view_report
            self.saveLogView();
            
        return dict(page='risk',util=self.util,year=year,listYear = listYear,section = section);
    
     
    
    @expose('risk.templates.risk.report3')
    def report3(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        set_lang("th");
        session['lang'] = "th";
        session.save();
        
        year = self.util.isValue(kw.get('year'));
        
         
        log.info(year);
        if year is None:
            year = self.defaultyear;
            
        listYear = self.util.getRangeYear(year);
         
                
        section=[];
        self.listSectionTeam = [];
        if(year):
            
             
            self.riskSectionTeam =  app_model.RiskTeam.listTeam(1);
            
            row=1;
            for sectionTeam in self.riskSectionTeam:
                self.listSectionTeam.append({'row':row,'risk_team_id':sectionTeam.risk_team_id ,
                                             'description':sectionTeam.description,
                                             'reported1':0,'total1':0,'reported2':0,'total2':0,
                                             'reported3':0,'total3':0,'reported4':0,'total4':0,
                                             'reported5':0,'total5':0,'reported6':0,'total6':0,
                                             'reported7':0,'total7':0,'reported8':0,'total8':0,
                                             'reported9':0,'total9':0,'reported10':0,'total10':0,
                                             'reported11':0,'total11':0,'reported12':0,'total12':0 ,
                                             'total_reported':0 ,'total':0});
                row = row+1;
                                        
            
            log.info("leng : " + str(len(self.listSectionTeam)));                            
            for month in range(10,13) :
                
                date = '1/'+str(month)+'/'+str(int(year)-543 -1);
                log.info("start : " + date);
                startDate = self.util.convertStringToDate(date);
                stopDate = self.util.last_day_of_month(startDate);
                
                startDate = startDate.strftime("%Y-%m-%d");
                stopDate = stopDate.strftime("%Y-%m-%d");
                 
                section =  app_model.RiskManagement.listSectionReported(startDate,stopDate);
                
                
                for sec in section:
                    for secTeam in self.listSectionTeam:
                        if(str(sec.get('risk_team_id')) == str(secTeam.get('risk_team_id'))):
                            log.info("same11111111");
                            secTeam['reported'+str(month) ] = sec.get('reported')  ;
                            secTeam['total'+ str(month)]   = sec.get('total')   ;
                            break;
                        
            for month in range(1,10) :
                
                date = '1/'+str(month)+'/'+str(int(year)-543 );
                log.info("start : " + date);
                startDate = self.util.convertStringToDate(date);
                stopDate = self.util.last_day_of_month(startDate);
                
                startDate = startDate.strftime("%Y-%m-%d");
                stopDate = stopDate.strftime("%Y-%m-%d");
                 
                section =  app_model.RiskManagement.listSectionReported(startDate,stopDate);
                
                
                for sec in section:
                    for secTeam in self.listSectionTeam:
                        if(str(sec.get('risk_team_id')) == str(secTeam.get('risk_team_id'))):
                            log.info("same11111111");
                            secTeam['reported'+str(month) ] = sec.get('reported')  ;
                            secTeam['total'+ str(month)]   = sec.get('total')   ;
                            break; 
                             
            
            for secTeam in self.listSectionTeam:
                    secTeam['total_reported']= int(secTeam['reported1'])+int(secTeam['reported2'])+int(secTeam['reported3'])+int(secTeam['reported4'])+int(secTeam['reported5'])+int(secTeam['reported6'])+int(secTeam['reported7'])+int(secTeam['reported8'])+int(secTeam['reported9'])+int(secTeam['reported10'])+int(secTeam['reported11'])+int(secTeam['reported12']);
                    secTeam['total']= int(secTeam['total1'])+int(secTeam['total2'])+int(secTeam['total3'])+int(secTeam['total4'])+int(secTeam['total5'])+int(secTeam['total6'])+int(secTeam['total7'])+int(secTeam['total8'])+int(secTeam['total9'])+int(secTeam['total10'])+int(secTeam['total11'])+int(secTeam['total12']);
            
            #log_view_report
            self.saveLogView();
            
             
        
        return dict(page='risk',util=self.util,year=year,listYear = listYear,section = self.listSectionTeam);
    
    @expose('risk.templates.risk.report4')
    def report4(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        set_lang("th");
        session['lang'] = "th";
        session.save();
        
        year = self.util.isValue(kw.get('year'));
        
        log.info(year);
        if year is None:
            year = self.defaultyear;
            
        listYear = self.util.getRangeYear(year);
                
        section=[];
        self.listSectionTeam = [];
        if(year):
            
            self.riskSectionTeam =  app_model.RiskTeam.listTeam(2);
            
            row=1;
            for sectionTeam in self.riskSectionTeam:
                self.listSectionTeam.append({'row':row,'risk_team_id':sectionTeam.risk_team_id ,
                                             'description':sectionTeam.description,
                                             'reported1':0,'total1':0,'reported2':0,'total2':0,
                                             'reported3':0,'total3':0,'reported4':0,'total4':0,
                                             'reported5':0,'total5':0,'reported6':0,'total6':0,
                                             'reported7':0,'total7':0,'reported8':0,'total8':0,
                                             'reported9':0,'total9':0,'reported10':0,'total10':0,
                                             'reported11':0,'total11':0,'reported12':0,'total12':0 ,
                                             'total_reported':0 ,'total':0});
                row = row+1;
                                        
            
            log.info("leng : " + str(len(self.listSectionTeam)));                            
            for month in range(10,13) :
                
                date = '1/'+str(month)+'/'+str(int(year)-543 - 1);
                log.info("start : " + date);
                startDate = self.util.convertStringToDate(date);
                stopDate = self.util.last_day_of_month(startDate);
                
                startDate = startDate.strftime("%Y-%m-%d");
                stopDate = stopDate.strftime("%Y-%m-%d");
                 
                section =  app_model.RiskManagement.listSectionReported(startDate,stopDate);
                
                
                for sec in section:
                    for secTeam in self.listSectionTeam:
                        if(str(sec.get('risk_team_id')) == str(secTeam.get('risk_team_id'))):
                            log.info("same11111111");
                            secTeam['reported'+str(month) ] = sec.get('reported')  ;
                            secTeam['total'+ str(month)]   = sec.get('total')   ;
                            break;
                        
            for month in range(1,10) :
                
                date = '1/'+str(month)+'/'+str(int(year)-543);
                log.info("start : " + date);
                startDate = self.util.convertStringToDate(date);
                stopDate = self.util.last_day_of_month(startDate);
                
                startDate = startDate.strftime("%Y-%m-%d");
                stopDate = stopDate.strftime("%Y-%m-%d");
                 
                section =  app_model.RiskManagement.listSectionReported(startDate,stopDate);
                
                
                for sec in section:
                    for secTeam in self.listSectionTeam:
                        if(str(sec.get('risk_team_id')) == str(secTeam.get('risk_team_id'))):
                            log.info("same11111111");
                            secTeam['reported'+str(month) ] = sec.get('reported')  ;
                            secTeam['total'+ str(month)]   = sec.get('total')   ;
                            break; 
                             
            
            for secTeam in self.listSectionTeam:
                    secTeam['total_reported']= int(secTeam['reported1'])+int(secTeam['reported2'])+int(secTeam['reported3'])+int(secTeam['reported4'])+int(secTeam['reported5'])+int(secTeam['reported6'])+int(secTeam['reported7'])+int(secTeam['reported8'])+int(secTeam['reported9'])+int(secTeam['reported10'])+int(secTeam['reported11'])+int(secTeam['reported12']);
                    secTeam['total']= int(secTeam['total1'])+int(secTeam['total2'])+int(secTeam['total3'])+int(secTeam['total4'])+int(secTeam['total5'])+int(secTeam['total6'])+int(secTeam['total7'])+int(secTeam['total8'])+int(secTeam['total9'])+int(secTeam['total10'])+int(secTeam['total11'])+int(secTeam['total12']);
            
             
            #log_view_report
            self.saveLogView();
            
            
        return dict(page='risk',util=self.util,year=year,listYear = listYear,section = self.listSectionTeam);
    
    @expose('risk.templates.risk.report5')
    def report5(self,**kw):
        
        reload(sys);
        sys.setdefaultencoding("utf-8");
        set_lang("th");
        session['lang'] = "th";
        session.save();
        
        sectionListTeam = None;
        sectionTeamId = 0;
        disabledSelect = False;
        userid = None;
        level = "1";
        
        self.team_id =  self.util.numValue( kw.get('team_id')) ;        
        self.datepickerStart =   self.util.isValue(kw.get('datepickerStart') );
        self.datepickerStop =   self.util.isValue(kw.get('datepickerStop') ); 
        
        #search section team id 
        if request.identity:
            userid = request.identity['repoze.who.userid'];
            section =  app_model.UserRiskSection.getByUserName(userid);
            if(section):
                sectionid = section.risk_section_id;
                section =  app_model.RiskSection.listBySectionbyId(sectionid);
                if(section):
                    userid = section.description;
                    level = "0";
                    sectionListTeam =  app_model.SectionListTeam.getSectionBySectionId(section.risk_section_id);
                    sectionTeamId = sectionListTeam.risk_team_id;
                    self.team_id = sectionTeamId;
                    disabledSelect = True;
        else:
            userid = None;       
        
        
        #convert date
        if( self.datepickerStart and self.datepickerStop) :
            self.datepickerStart  = self.util.convertStringDateToString(  self.datepickerStart,  "%Y-%m-%d") ;
            self.datepickerStop =self.util.convertStringDateToString( self.datepickerStop,  "%Y-%m-%d");
        else:
            if(self.datepickerStart ):
                self.datepickerStart  = self.util.convertStringDateToString(  self.datepickerStart,  "%Y-%m-%d") ;
            if(self.datepickerStop ): 
                self.datepickerStop =self.util.convertStringDateToString( self.datepickerStop,  "%Y-%m-%d");
            if(self.datepickerStart is None and self.datepickerStop is None) :
                self.datepickerStart  = self.util.convertStringDateToString(  self.datepickerStart,  "%Y-%m-%d") ;
                self.datepickerStop =self.util.convertStringDateToString( self.datepickerStop,  "%Y-%m-%d");
        
        
        #find listteam
        self.listTeam =  app_model.RiskTeam.listTeamCrom();
        
        self.listTeamCrom = [];
        self.teamName = "";
        self.listRiskTeamCrom = []
        
        for temp in self.listTeam:
            if( int(self.team_id) == int(temp.risk_team_id)  or int(sectionTeamId) == int(temp.risk_team_id) ):
                self.teamName = temp.description;
                self.listTeamCrom.append( { "risk_team_id" : temp.risk_team_id ,  "description"  :temp.description , "selected" : True });
            else:
                self.listTeamCrom.append( { "risk_team_id" : temp.risk_team_id ,  "description"  :temp.description , "selected" : False });
       
        #search risk in team crom
        if self.team_id :
            self.listRiskTeamCrom =  app_model.RiskManagement.showRiskRespTeamCromManage(self.team_id, self.datepickerStart, self.datepickerStop);          
   
        
        #log_view_report
        self.saveLogView();
            
        
        return dict(listteam = self.listTeamCrom,disabledSelect =disabledSelect, 
                    level = level ,util=self.util,teamName = self.teamName , 
                    start = self.datepickerStart , stop = self.datepickerStop, 
                    riskTeamCrom = self.listRiskTeamCrom  );
    
    
    @expose('risk.templates.risk.report6')
    def report6(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        set_lang("th");
        session['lang'] = "th";
        session.save();
        
        year = self.util.isValue(kw.get('year'));
        
        month = self.util.isValue(kw.get('month'));
        listMonth =[];
        listMonth.append({'id':'1','value':'มกราคม'});
        listMonth.append({'id':'2','value':'กุมภาพันธ์'});
        listMonth.append({'id':'3','value':'มีนาคม'});
        listMonth.append({'id':'4','value':'เมษายน'});
        listMonth.append({'id':'5','value':'พฤษภาคม'});
        listMonth.append({'id':'6','value':'มิถุนายน'});
        listMonth.append({'id':'7','value':'กรกฎาคม'});
        listMonth.append({'id':'8','value':'สิงหาคม'});
        listMonth.append({'id':'9','value':'กันยายน'});
        listMonth.append({'id':'10','value':'ตุลาคม'});
        listMonth.append({'id':'11','value':'พฤศจิกายน'});
        listMonth.append({'id':'12','value':'ธันวาคม'});
        
        log.info(year);
        if year is None:
            year = self.defaultyear;
            
        listYear = self.util.getRangeYear(year);
        
        stopDate = None;
        startDate = None;
        listReponsible=[] 
        program=[]
        if (month and year):
            print month;
            print year;
            date = '1/'+str(month)+'/'+str(int(year)-543);
            startDate = self.util.convertStringToDate(date);
            stopDate = self.util.last_day_of_month(startDate);
            
            startDate = startDate.strftime("%Y-%m-%d");
            stopDate = stopDate.strftime("%Y-%m-%d");
            listReponsible,program =  app_model.RiskManagement.listResponsibleInTime(risk_team_type = 1, risk_program = 1, startDate = startDate, stopDate=stopDate)

        self.saveLogView();
        
        return dict(report = '', year=year, month=month, listMonth=listMonth, listYear = listYear,
                    util=self.util,program=program,
                    fiscal_year = self.util.calFiscalYear(month, year),
                    startDate=startDate, stopDate = stopDate, listReponsible=listReponsible);
    
    @expose('risk.templates.risk.report7')
    def report7(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        set_lang("th");
        session['lang'] = "th";
        session.save();
        
        year = self.util.isValue(kw.get('year'));
        
        month = self.util.isValue(kw.get('month'));
        listMonth =[];
        listMonth.append({'id':'1','value':'มกราคม'});
        listMonth.append({'id':'2','value':'กุมภาพันธ์'});
        listMonth.append({'id':'3','value':'มีนาคม'});
        listMonth.append({'id':'4','value':'เมษายน'});
        listMonth.append({'id':'5','value':'พฤษภาคม'});
        listMonth.append({'id':'6','value':'มิถุนายน'});
        listMonth.append({'id':'7','value':'กรกฎาคม'});
        listMonth.append({'id':'8','value':'สิงหาคม'});
        listMonth.append({'id':'9','value':'กันยายน'});
        listMonth.append({'id':'10','value':'ตุลาคม'});
        listMonth.append({'id':'11','value':'พฤศจิกายน'});
        listMonth.append({'id':'12','value':'ธันวาคม'});
        
        log.info(year);
        if year is None:
            year = self.defaultyear;
            
        listYear = self.util.getRangeYear(year);
        
        stopDate = None;
        startDate = None;
        listReponsible=[] 
        program=[]
        if (month and year):
            print month;
            print year;
            date = '1/'+str(month)+'/'+str(int(year)-543);
            startDate = self.util.convertStringToDate(date);
            stopDate = self.util.last_day_of_month(startDate);
            
            startDate = startDate.strftime("%Y-%m-%d");
            stopDate = stopDate.strftime("%Y-%m-%d");
        
        
        
            listReponsible,program =  app_model.RiskManagement.listResponsibleInTime(risk_team_type = 2, risk_program = 1, startDate = startDate, stopDate=stopDate)
        
         
        self.saveLogView();
        
        return dict(report = '', year=year, month=month, listMonth=listMonth, listYear = listYear,
                    util=self.util,program=program,
                    fiscal_year = self.util.calFiscalYear(month, year),
                    startDate=startDate, stopDate = stopDate, listReponsible=listReponsible);  
    
    @expose('risk.templates.risk.report8')
    def report8(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        set_lang("th");
        session['lang'] = "th";
        session.save();
        
        year = self.util.isValue(kw.get('year'));
        
        month = self.util.isValue(kw.get('month'));
        listMonth =[];
        listMonth.append({'id':'1','value':'มกราคม'});
        listMonth.append({'id':'2','value':'กุมภาพันธ์'});
        listMonth.append({'id':'3','value':'มีนาคม'});
        listMonth.append({'id':'4','value':'เมษายน'});
        listMonth.append({'id':'5','value':'พฤษภาคม'});
        listMonth.append({'id':'6','value':'มิถุนายน'});
        listMonth.append({'id':'7','value':'กรกฎาคม'});
        listMonth.append({'id':'8','value':'สิงหาคม'});
        listMonth.append({'id':'9','value':'กันยายน'});
        listMonth.append({'id':'10','value':'ตุลาคม'});
        listMonth.append({'id':'11','value':'พฤศจิกายน'});
        listMonth.append({'id':'12','value':'ธันวาคม'});
        
        log.info(year);
        if year is None:
            year = self.defaultyear;
            
        listYear = self.util.getRangeYear(year);
        
        stopDate = None;
        startDate = None;
        listReponsible=[] 
        program=[]
        if (month and year):
            print month;
            print year;
            date = '1/'+str(month)+'/'+str(int(year)-543);
            startDate = self.util.convertStringToDate(date);
            stopDate = self.util.last_day_of_month(startDate);
            
            startDate = startDate.strftime("%Y-%m-%d");
            stopDate = stopDate.strftime("%Y-%m-%d");
        
            print "self.startDate = %s, stopDate = %s" %(startDate, stopDate)
            
        
            listReponsible,program =  app_model.RiskManagement.listResponsibleInTime(risk_team_type = 1, risk_program = 0, startDate = startDate, stopDate=stopDate)
        
         
        self.saveLogView();
        
        return dict(report = '', year=year, month=month, listMonth=listMonth, listYear = listYear,
                    util=self.util,program=program,
                    fiscal_year = self.util.calFiscalYear(month, year),
                    startDate=startDate, stopDate = stopDate, listReponsible=listReponsible);  
    
    @expose('risk.templates.risk.report9')
    def report9(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        set_lang("th");
        session['lang'] = "th";
        session.save();
        
        year = self.util.isValue(kw.get('year'));
        
        month = self.util.isValue(kw.get('month'));
        listMonth =[];
        listMonth.append({'id':'1','value':'มกราคม'});
        listMonth.append({'id':'2','value':'กุมภาพันธ์'});
        listMonth.append({'id':'3','value':'มีนาคม'});
        listMonth.append({'id':'4','value':'เมษายน'});
        listMonth.append({'id':'5','value':'พฤษภาคม'});
        listMonth.append({'id':'6','value':'มิถุนายน'});
        listMonth.append({'id':'7','value':'กรกฎาคม'});
        listMonth.append({'id':'8','value':'สิงหาคม'});
        listMonth.append({'id':'9','value':'กันยายน'});
        listMonth.append({'id':'10','value':'ตุลาคม'});
        listMonth.append({'id':'11','value':'พฤศจิกายน'});
        listMonth.append({'id':'12','value':'ธันวาคม'});
        
        log.info(year);
        if year is None:
            year = self.defaultyear;
            
        listYear = self.util.getRangeYear(year);
        
        stopDate = None;
        startDate = None;
        listReponsible=[] 
        program=[]
        if (month and year):
            print month;
            print year;
            date = '1/'+str(month)+'/'+str(int(year)-543);
            startDate = self.util.convertStringToDate(date);
            stopDate = self.util.last_day_of_month(startDate);
            
            startDate = startDate.strftime("%Y-%m-%d");
            stopDate = stopDate.strftime("%Y-%m-%d");
        
        
        
            listReponsible,program =  app_model.RiskManagement.listResponsibleInTime(risk_team_type = 2, risk_program = 0, startDate = startDate, stopDate=stopDate)
        
         
        self.saveLogView();
        
        return dict(report = '', year=year, month=month, listMonth=listMonth, listYear = listYear,
                    util=self.util,program=program,
                    fiscal_year = self.util.calFiscalYear(month, year),
                    startDate=startDate, stopDate = stopDate, listReponsible=listReponsible);  
        

    
    @expose('json')
    def getUser(self,**kw):
        if request.identity:
            userid = request.identity['repoze.who.userid'];
        else:
            userid = None;
        listuser  = {'id':userid,'name':userid};
        return dict(root = listuser );
    
    @expose('json')
    def listRiskLevel(self ,**kw):
         
        self.risk_program_group_id = self.util.isValue(kw.get('risk_program_group_id')); 
        
        
        if(self.risk_program_group_id == '2'):
            self.listLevel =  app_model.RiskLevel.listRiskByPhysical();
        else:
            self.listLevel =  app_model.RiskLevel.listRiskByClinical();
            
        self.listDataRiskLevel = [];
        self.listDataRiskLevel.append({'id':'0','name':'*'});
        if(self.listLevel):
            for value in self.listLevel:
                self.listDataRiskLevel.append({'id':value.risk_level_id,'name':value.description +" " + self.util.valueNull(value.effective) }); 
        return dict(root = self.listDataRiskLevel,total=str(len(self.listDataRiskLevel)));
    
    @expose('json')
    def listTeamRespose(self,**kw):
        self.team_type = self.util.isValue(kw.get('team_type')); 
        self.riskTeam =  app_model.RiskTeam.listTeamByActive(self.team_type);
        self.list = [];
        if(self.riskTeam):
            for value in self.riskTeam:
                self.list.append({'id':value.risk_team_id,'name':value.description}); 
        return dict(root = self.list,total=str(len(self.list)));
    
    @expose('json')
    def listTeamResponseAll(self,**kw):
        
        self.riskTeam =  app_model.RiskTeam.listTeam( );
        self.list = [];
        if(self.riskTeam):
            for value in self.riskTeam:
                self.list.append({'id':value.risk_team_id,'name':value.description,
                                  'type':value.risk_team_type_id ,'type_name':value.risk_team_type.description }); 
        return dict(root = self.list,total=str(len(self.list)));
    
    @expose('json')
    def listTeamResponseTypeAll(self,**kw): 
        self.riskTeamtype =  app_model.RiskTeamType.listTeamTypeAll();
         
        self.list = [];
        if(self.riskTeamtype):
            for value in self.riskTeamtype:
                self.list.append({'id':value.risk_team_type_id,'name':value.description  }); 
        return dict(root = self.list,total=str(len(self.list)));
    
    @expose('json')
    def listProgramsAll(self,**kw):
        
        self.riskTeam =  app_model.RiskProgramDetail.listAll( );
        self.list = [];
        if(self.riskTeam):
            for value in self.riskTeam:
                self.list.append({'id':value.risk_program_detail_id,'name':value.description,
                                  'type':value.risk_program_group_id ,'type_name':value.risk_program_group.description }); 
        return dict(root = self.list,total=str(len(self.list)));
    
    @expose('json')
    def listProgramsTypeAll(self,**kw): 
        self.riskTeamtype =  app_model.RiskProgramGroup.listAll();
         
        self.list = [];
        if(self.riskTeamtype):
            for value in self.riskTeamtype:
                self.list.append({'id':value.risk_program_group_id,'name':value.description  }); 
        return dict(root = self.list,total=str(len(self.list)));
    
    @expose('json')
    def listRiskLevelAll(self,**kw):
        
        self.listData =  app_model.RiskLevel.listAll( );
        self.list = [];
        if(self.listData):
            for value in self.listData:
            
                
                self.list.append({'id':value.risk_level_id,'name':value.description,
                                  'eff':value.effective ,'type': value.risk_program_group_id, 'type_name':value.risk_program_group.description }); 
        return dict(root = self.list,total=str(len(self.list)));
    
    @expose('json')
    def listRiskStatus(self,**kw):
        self.listType =  app_model.RiskStatus.listAll();
        self.list = [];
        self.list.append({'id':'0','name':'*'});
        if(self.listType):
            for value in self.listType:
                self.list.append({'id':value.risk_status_id,'name':value.description}); 
        return dict(root = self.list,total=str(len(self.list)));
    
    
    
    @expose('json')
    def listSection(self ,**kw):
        section_id = self.util.isValue(kw.get('section_id'));
        self.list = [];
        if(section_id is None):
            self.listType =  app_model.RiskSection.listAll();
            self.list.append({'id':'0','name':'*'});
             
        else:
            self.listType =  app_model.RiskSection.listBySection(section_id);
        
        if(self.listType):
                for value in self.listType:
                    self.list.append({'id':value.risk_section_id,'name':value.description}); 
                        
        return dict(root = self.list,total=str(len(self.list)));
    
    
    @expose('json')
    def listProgramGroup(self ,**kw):
        self.listType =  app_model.RiskProgramGroup.listAll();
        self.list = [];
        self.list.append({'id':'0','name':'*'});
        if(self.listType):
            for value in self.listType:
                self.list.append({'id':value.risk_program_group_id,'name':value.description}); 
        return dict(root = self.list,total=str(len(self.list)));
    
    @expose('json')
    def listProgramDetail (self, **kw):
        listProgramDetail = [];
        listProgramDetail.append({'id':'0','name':'*'});
        groupId = self.util.isValue(kw.get('risk_program_group_id'));
        if(groupId is None):
            groupId = '1';
        listType =  app_model.RiskProgramDetail.listAllByGroup(groupId);
        if(listType):
            for value in listType:
                listProgramDetail.append({'id':value.risk_program_detail_id,'name':value.description}); 
        return dict(root = listProgramDetail,total=str(len(listProgramDetail)));
    
    @expose('json')
    def showRiskRespManage(self,**kw):
        self.list = [];
        
        self.startDate = self.util.spitStringDate(kw.get('startDate'));
        self.stopDate = self.util.spitStringDate(kw.get('stopDate'));
        self.riskSection = self.util.isValue(kw.get('riskSection'));
        self.riskProgramGroup = self.util.isValue(kw.get('riskProgramGroup'));
        self.riskStatus = self.util.isValue(kw.get('riskStatus'));
        self.riskProgramDetail= self.util.isValue(kw.get('riskProgramDetail'));
        self.riskId= self.util.isValue(kw.get('riskJobId'));
        
        log.info(self.startDate);
        log.info(self.stopDate);
        log.info(self.riskSection);
        log.info(self.riskProgramGroup);
        log.info(self.riskStatus);
        log.info(self.riskProgramDetail);
        log.info(self.riskId);
         
        self.list =  app_model.RiskManagement.showRiskRespManage(self.startDate, self.stopDate, self.riskSection, self.riskProgramGroup, self.riskStatus,self.riskProgramDetail ,self.riskId );
        
        return dict(root = self.list,total=str(len(self.list)));
    
    @expose('json')
    def showRiskManage(self,**kw):
        self.startDate = self.util.spitStringDate(kw.get('startDate'));
        self.stopDate = self.util.spitStringDate(kw.get('stopDate'));
        self.riskSection = self.util.isValue(kw.get('riskSection'));
        self.riskProgramGroup = self.util.isValue(kw.get('riskProgramGroup'));
        self.riskStatus = self.util.isValue(kw.get('riskStatus'));
        self.riskProgramDetail= self.util.isValue(kw.get('riskProgramDetail'));
        self.riskId= self.util.isValue(kw.get('riskJobId'));
        
        log.info(self.startDate);
        log.info(self.stopDate);
        log.info(self.riskSection);
        log.info(self.riskProgramGroup);
        log.info(self.riskStatus);
        log.info(self.riskProgramDetail);
        log.info(self.riskId);
        
        
        self.list =  app_model.RiskManagement.showRiskManage(self.startDate, self.stopDate, self.riskSection, self.riskProgramGroup, self.riskStatus,self.riskProgramDetail ,self.riskId );
        
        return dict(root = self.list,total=str(len(self.list)));
    @expose('json')
    def createRisk(self, **kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        self.message ="sucess";
        self.success = True;
        try:
            log.info("create risk");
            log.info(kw);
            #kw.get('risk_management_id');
            self.risk_level = kw.get('risk_level_id');
            self.risk_program = kw.get('risk_program');
            self.risk_section = kw.get('risk_section_id');
            self.detail = kw.get('detail');
            self.report_date = self.util.convertStringToDate(kw.get('report_date')) ;
            self.risk_program_detail = kw.get('risk_program_detail_id');
            self.risk_management_id = self.util.isValue(kw.get('risk_management_id'));
            self.risk_solution = kw.get('risk_solution');
            #response teams
            self.crom_team = self.util.isValue(kw.get('crom_team'));
            self.section_team = self.util.isValue(kw.get('section_team'));
            
             
            if(self.risk_management_id ):
                #check admin = 1 , user= 0;
                self.level = self.util.isValue(kw.get('level'));
                log.info("level : " + str(self.level));
                 
                
                self.risk =  app_model.RiskManagement.getById(self.risk_management_id);
                self.risk.detail = self.detail;
                self.risk.solution = self.risk_solution;
                self.risk.risk_level_id = self.risk_level;
                self.risk.risk_section_id = self.risk_section;
                self.risk.risk_program_detail_id = self.risk_program_detail;
                
                #change status  and check level is admin then change status = 2
                
                if(self.level is not None and str(self.level) == str(1) ):
                    log.info("change status :");
                    if(self.risk.risk_status_id == 1):
                        self.risk.risk_status_id = 2 ;
                 
                log.info("=====save=====");
                app_model.RiskResponsible.saveByTeam(self.crom_team, self.risk.risk_management_id);
                app_model.RiskResponsible.saveByTeam(self.section_team, self.risk.risk_management_id);
                #remove
                cteam = "";
                steam = "";
                if(self.crom_team):
                    cteam = self.crom_team.split(',');
                if(self.section_team):
                    steam  = self.section_team.split(',');
                
                remove_Respon = "";
                for d in cteam:
                    remove_Respon = d +"," +remove_Respon;
                for d in steam:
                    remove_Respon = d +"," +remove_Respon;
                
                if(len(remove_Respon) >0 ):
                    remove_Respon = remove_Respon[:-1];
                    app_model.RiskResponsible.removeExclusiveOf(remove_Respon, self.risk.risk_management_id);
                else:#remove all
                    app_model.RiskResponsible.removeRiskManage(self.risk.risk_management_id);
                       
                log.info(remove_Respon);
            else:#insert
                self.risk =  app_model.RiskManagement();
                self.risk.detail = self.detail;
                self.risk.solution = self.risk_solution;
                self.risk.risk_level_id = self.risk_level;
                self.risk.risk_section_id = self.risk_section;
                self.risk.risk_program_detail_id = self.risk_program_detail;
                self.risk.risk_status_id = 1;
                self.risk.report_date =  self.report_date;
                self.risk.save();
                
                log.info("=====save=====");
                app_model.RiskResponsible.saveByTeam(self.crom_team, self.risk.risk_management_id);
                app_model.RiskResponsible.saveByTeam(self.section_team, self.risk.risk_management_id);
                
                self.riskservice.notifyByLevel(self.risk)
         
        except Exception, exception:
            log.info("error : " + str(exception));
            self.message ="fail";
            self.success = False;
            log.info("create risk");
            log.info(kw);
            
        return dict(success=self.success, message = self.message);
    
 
    
    @expose('json')
    def sendTeam(self,**kw):
        self.message ="sucess";
        self.success = True;
        try:
            log.info("create risk");
            log.info(kw);
            #kw.get('risk_management_id');
            self.risk_level = kw.get('risk_level_id');
            self.risk_program = kw.get('risk_program');
            self.risk_section = kw.get('risk_section_id'); 
            self.detail = kw.get('detail');
            self.report_date = self.util.convertStringToDate(kw.get('report_date')) ;
            self.risk_program_detail = kw.get('risk_program_detail_id');
            self.risk_management_id = self.util.isValue(kw.get('risk_management_id'));
             
             
                
            self.risk_status = self.util.isValue(kw.get('risk_status_id'));
            
            self.crom_team = self.util.isValue(kw.get('crom_team'));
            self.section_team = self.util.isValue(kw.get('section_team'));
            
            
            self.risk =  app_model.RiskManagement.getById(self.risk_management_id);
            self.risk.detail = self.detail;
            self.risk.risk_level_id = self.risk_level;
            self.risk.risk_section_id = self.risk_section;
            self.risk.risk_program_detail_id = self.risk_program_detail;
            
            if(self.risk.risk_status_id <3):
                self.risk.risk_status_id = 3; 
            
             
            #self.risk.risk_status_id = 1;
            #self.risk.report_date =  self.report_date;
            log.info("=====save=====");
            app_model.RiskResponsible.saveByTeam(self.crom_team, self.risk.risk_management_id);
            app_model.RiskResponsible.saveByTeam(self.section_team, self.risk.risk_management_id);
            log.info(self.crom_team);
             
         
        except Exception, exception:
            log.info("error : " + str(exception));
            self.message ="fail";
            self.success = False;
            
        return dict(success=self.success, message = self.message);
    
    @expose('json')
    def findRiskResponsible(self, **kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        self.listresponse = [];
        #self.risk_team = self.util.isValue(kw.get('risk_team')); 
        self.risk_team = self.util.getArrayComma(kw.get('risk_team'));
        self.risk_namager = self.util.isValue(kw.get('risk_namager'));
        self.riskResponse =  app_model.RiskResponsible.listByTeamsAndRiskManage(self.risk_team,self.risk_namager );
        if(self.riskResponse):
            for value in self.riskResponse:
                self.listresponse.append({'id':value.risk_team_id,'name':value.risk_team.description,'detail':value.detail}); 
                 
        return dict(root = self.listresponse,total=str(len(self.listresponse)));
    
    @expose('json')
    def findRiskResponsible_old(self, **kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        
        self.risk_team = self.util.isValue(kw.get('risk_team')); 
        self.risk_namager = self.util.isValue(kw.get('risk_namager'));
        name= self.util.isValue(kw.get('name'));
        self.riskResponse =  app_model.RiskResponsible.getTeamByTeamTypeAndRiskManage(self.risk_team,self.risk_namager );
        self.list = [];
        if(self.riskResponse):
            for value in self.riskResponse:
                self.list.append({'id':value.risk_team_id,'name':name,'detail':value.detail}); 
        return dict(root = self.list,total=str(len(self.list)));
  
    @expose('json')
    def listResponByUser(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        
        self.user = self.util.isValue(kw.get('user')); 
        
        self.users =  self.user.split(",");
        
        self.riskResponse =[];
        row_record = 1;
        self.list= [];
        if(len(self.users) >1  ) :
            
            print self.users ;
            
            for user in self.users:
                self.riskSection =  app_model.UserRiskSection.getSectionByUser(user);
                self.riskResponse =  app_model.RiskManagement.showRiskRespManage(None, None, str(self.riskSection ), None, None,None ,None );
                
                for row in self.riskResponse:
                    self.list.append({'row':row_record, 'risk_management_id':row['risk_management_id'],  
                              'risk_responsible_id':row['risk_responsible_id'], 
                              'risk_detail':row['risk_detail'], 
                               'ans':row['detail'] });
                    row_record = row_record +1;
       
       
        else:
            #find section_id by user name
            self.riskSection =  app_model.UserRiskSection.getSectionByUser(self.user);
            self.riskResponse =  app_model.RiskManagement.showRiskRespManage(None, None, str(self.riskSection ), None, None,None ,None );
        
            for row in self.riskResponse:
                self.list.append({'row':row_record, 'risk_management_id':row['risk_management_id'],  
                              'risk_responsible_id':row['risk_responsible_id'], 
                              'risk_detail':row['risk_detail'], 
                               'ans':row['detail'] });
                row_record = row_record +1;

         
        return dict(root =  self.list,total=str(len( self.list)));
     
    @expose('json')
    def replyRisk(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        self.message ="sucess";
        self.success = True; 
        try:
            #self.risk_level = kw.get('risk_level_id');
            #self.risk_program = kw.get('risk_program');
            #self.risk_section = kw.get('risk_section_id');
            #self.detail = kw.get('detail');
            #self.report_date = self.util.convertStringToDate(kw.get('report_date')) ;
            #self.risk_program_detail = kw.get('risk_program_detail');
            self.risk_management_id = self.util.isValue(kw.get('risk_management_id'));
             
            if(self.risk_management_id ):
                
                self.risk_status = self.util.isValue(kw.get('risk_status_id'));
                
                self.crom_team = self.util.isValue(kw.get('crom_team'));
                self.section_team = self.util.isValue(kw.get('section_team'));
                
                
                #self.risk = RiskManagement.getById(self.risk_management_id);
                reply_success = False;
                log.info("-------update crom_team");
                if(self.crom_team):
                    listteam = self.crom_team.split(',');
                    
                    for team in listteam:
                        details = self.util.isValue(kw.get('details'+str(team))); 
                        if(details):          
                            reply_success = True;         
                            app_model.RiskResponsible.updateDetailByTeamAndRisk(team, self.risk_management_id, details);
                         
                            log.info("update : " + team);
                log.info("-------update section_team");
                if(self.section_team):
                    listteam = self.section_team.split(',');
                    for team in listteam:
                        details = self.util.isValue(kw.get('details'+str(team)));
                        if(details):      
                            reply_success = True;              
                            app_model.RiskResponsible.updateDetailByTeamAndRisk(team, self.risk_management_id, details);
                            log.info("update : " + team);
                         
                #reply_success
                if(reply_success == True):
                    self.risk =  app_model.RiskManagement.getById(self.risk_management_id);
                    if(self.risk.risk_status_id == 3):
                        self.risk.risk_status_id = 4;
                        
                    if( app_model.RiskManagement.checkResponsible(self.risk_management_id)):
                        self.risk.risk_status_id = 5;
                #log.info(self.crom_team);
                
        except Exception, exception:
            log.info("error : " + str(exception));
            self.message ="fail";
            self.success = False;
            
        return dict(success=self.success, message = self.message);
    
    @expose('json')
    def deleteRisk(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        self.message ="sucess";
        self.success = True;
        try:
            log.info("delete risk");
            log.info(kw);
             
            self.risk_management_id = self.util.isValue(kw.get('risk_management_id'));
            
           
             
            if(self.risk_management_id ):
                
                self.risk_status = self.util.isValue(kw.get('risk_status_id')); 
                
                self.risk =  app_model.RiskManagement.getById(self.risk_management_id);
                #remove responsible
                app_model.RiskResponsible.removeRiskManage(self.risk_management_id);
                #remove risk
                self.risk.remove();
                            
         
        except Exception, exception:
            log.info("error : " + str(exception));
            self.message ="fail";
            self.success = False;
            
        return dict(success=self.success, message = self.message);
    
    
    @expose('json')
    def showDetailReportedByMonth(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        self.riskResponse =[];
        self.report_date =  datetime.now().strftime('%Y-%m');  
        self.riskResponse =  app_model.RiskManagement.showDetailReportedByMonth( self.report_date +"%");
        return dict(root =  self.riskResponse,total=str(len( self.riskResponse)));
    
    @expose('json')
    def exportReport1(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        
        print "exportReport 1";
        
        self.tableNo = self.util.isValue( kw.get('tableNo') ) ;
        self.startDate = self.util.isValue( kw.get('startDate') ) ;
        self.stopDate = self.util.isValue( kw.get('stopDate') ) ;
        self.pathfile ="";
        priority10 = [];
        reportname= "_";
        if( int(self.tableNo) == int(3) ):
            priority10 =  app_model.RiskManagement.listRiskPriority10(self.startDate,self.stopDate);
            reportname = reportname + "ทางคลินิก";
        else:
            priority10 =  app_model.RiskManagement.listRiskPriority10Physic(self.startDate,self.stopDate);
            reportname = reportname + "ทางกายภาพ";
            
        self.pathfile = self.export.exportReport1ToExcel(priority10);
      
        response.content_type = 'application/ms-excel'
        response.headers["Content-Disposition"] = "attachment;filename=report1"+reportname+".xls"
         
        fileData = open(self.pathfile,'rb');
        read_data = fileData.read();
        fileData.close()
        del fileData
        return read_data;    
    
    @expose(content_type="application/ms-excel")
    def exportReport5(self,**kw):
        self.team_id = self.util.isValue( kw.get('team_id') ) ;
        self.startDate = self.util.isValue( kw.get('startDate') ) ;
        self.stopDate = self.util.isValue( kw.get('stopDate') ) ;
        
        self.pathfile = "";    
        if self.team_id :            
            self.listRiskTeamCrom =  app_model.RiskManagement.showRiskRespTeamCromManage(self.team_id, self.startDate, self.stopDate);      
            self.pathfile = self.export.exportReport5ToExcel(self.listRiskTeamCrom);
            
            response.content_type = 'application/ms-excel'
            response.headers["Content-Disposition"] = "attachment;filename=report5.xls"
         
        fileData = open(self.pathfile,'rb');
        read_data = fileData.read();
        fileData.close()
        del fileData
        return read_data;
   
    
    @expose('json')
    def testShowResponse(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        
        listRiskManagement=  app_model.RiskManagement.showRiskRespTeamCromManage('73',   '2012-10-01'  ,'2012-11-31'  );
        #self.export.exportToExcel(list);
        self.export.exportReport5ToExcel(listRiskManagement);
