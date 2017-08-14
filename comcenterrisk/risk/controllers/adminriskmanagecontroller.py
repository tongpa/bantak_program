# -*- coding: utf-8 -*-
from tg import TGController
from tg import expose, flash, require, url, lurl, request, redirect, validate, session, response

from tg.i18n import ugettext as _, lazy_ugettext as l_, set_lang,get_lang
from tgext.pluggable import app_model
#from comcenter.model import  User, UserRiskSection,RiskManagement,LogviewReport,RiskSection, RiskTeam 
#from comcenter.model import SectionListTeam, RiskLevel, RiskTeamType, RiskProgramDetail, RiskProgramGroup, RiskStatus, RiskResponsible

from datetime import datetime

from comcenter.controllers.util.utility import Utility
#from comcenter.controllers.util.exportexcel.risktoexcel import RiskToExcel


import logging;
import sys;
log = logging.getLogger(__name__);


#from repoze.what.predicates import has_permission;
from tg import predicates
from tgext.admin import AdminController;
 



import logging;
import sys;
log = logging.getLogger(__name__);
__all__ = ['AdminRiskManageController']

 


class AdminRiskManageController(AdminController):
    
    #allow_only = has_permission('manage');
    #allow_only = predicates.has_permission('manage',msg='Only administrators can access.') #.not_anonymous() #
    
    def __init__(self):
        self.util = Utility();
       
        self.defaultyear = 2557;
    
    @expose('risk.templates.risk.admin.index')
    def index(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login', params=dict(came_from='/', __logins=login_counter))
        
        return dict(page='admin' );
  
    
    @expose('risk.templates.risk.admin.sectionmanage')
    def sectionmanage(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login', params=dict(came_from='/', __logins=login_counter))
        
        return dict(page='admin' );
    
    @expose('risk.templates.risk.admin.sectionteams')
    def sectionteams(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login', params=dict(came_from='/', __logins=login_counter))
        
        
        return dict(page='admin');
    
    @expose('risk.templates.risk.admin.programs')
    def programs(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login', params=dict(came_from='/', __logins=login_counter))
        
        
        return dict(page='admin');
    
    @expose('risk.templates.risk.admin.risklevel')
    def riskLevel(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");       
        
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login', params=dict(came_from='/', __logins=login_counter))
        
        return dict(page='admin');
    
    @expose('risk.templates.risk.admin.usermanage')
    def usermanage(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");       
        
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login', params=dict(came_from='/', __logins=login_counter))
        
        return dict(page='admin');
    
    @expose('json')
    def saveSection(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        self.message ="sucess";
        self.success = True;
        try:
            log.info("create section");
            log.info(kw);
             
            self.section_id   = self.util.isValue(kw.get('risk_section_id'));
            self.section_name = self.util.isValue(kw.get('detail_section'));
            
            if(self.section_id is not None):
                log.info("update section");
                section = app_model.RiskSection.listBySectionbyId(self.section_id);
                section.description = self.section_name;
               
            else:
                section = app_model.RiskSection();
                log.info("add section"); 
                section.description = self.section_name;
                section.save();
            
            print self.section_name
         
        except Exception, exception:
            log.info("error : " + str(exception));
            print exception;
            self.message ="fail";
            self.success = False;
            log.info("create risk");
            log.info(kw);
            
        return dict(success=self.success, message = self.message);
    
    @expose('json')
    def deleteSection(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        self.message ="sucess";
        self.success = True;
        try:
            log.info("delete section");
            log.info(kw);
             
            self.section_id   = self.util.isValue(kw.get('risk_section_id'));
            self.section_name = self.util.isValue(kw.get('detail_section'));
            
            if(self.section_id is not None):
                log.info("update section");
                section = app_model.RiskSection.listBySectionbyId(self.section_id);
                section.remove(); 
               
      
         
        except Exception, exception:
            log.info("error : " + str(exception));
            print exception;
            self.message ="fail";
            self.success = False;
            log.info("delete section");
            log.info(kw);
            
        return dict(success=self.success, message = self.message);
    
    
    @expose('json')
    def saveSectionTeam(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        self.message ="sucess";
        self.success = True;
        try:
            log.info("create team");
            log.info(kw);
             
            self.section_team_id   = self.util.isValue(kw.get('id'));
            self.section_team_name = self.util.isValue(kw.get('name'));
            self.section_team_type = self.util.isValue(kw.get('type'));
             
            if(self.section_team_id is not None):
                log.info("update team");
                riskteam = app_model.RiskTeam.getById(self.section_team_id);
                riskteam.description = self.section_team_name;
                riskteam.risk_team_type_id = self.section_team_type;
            else:
                riskteam = app_model.RiskTeam();
                log.info("add team"); 

                riskteam.description = self.section_team_name;
                riskteam.risk_team_type_id = self.section_team_type;
                riskteam.save();
            
        except Exception, exception:
            log.info("error : " + str(exception));
            print exception;
            self.message ="fail";
            self.success = False;
            log.info("create risk");
            log.info(kw);
            
        return dict(success=self.success, message = self.message);
    
    
    @expose('json')
    def deleteSectionTeam(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        self.message ="sucess";
        self.success = True;
        try:
            log.info("delete section");
            log.info(kw);
             
            self.section_team_id   = self.util.isValue(kw.get('id'));
            self.section_team_name = self.util.isValue(kw.get('name'));
            self.section_team_type = self.util.isValue(kw.get('type'));
            
            if(self.section_team_id is not None):
                log.info("delete section team");
                section = app_model.RiskTeam.getById(self.section_team_id);
                section.remove(); 
               
      
         
        except Exception, exception:
            log.info("error : " + str(exception));
            print exception;
            self.message ="fail";
            self.success = False;
            log.info("delete section team");
            log.info(kw);
            
        return dict(success=self.success, message = self.message);
    
    @expose('json')
    def savePrograms(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        self.message ="sucess";
        self.success = True;
        try:
            log.info("create team");
            log.info(kw);
             
            self.programs_id   = self.util.isValue(kw.get('id'));
            self.programs_name = self.util.isValue(kw.get('name'));
            self.programs_type = self.util.isValue(kw.get('type'));
             
            if(self.programs_id is not None):
                log.info("update team");
                riskteam = app_model.RiskProgramDetail.getById(self.programs_id);
                riskteam.description = self.programs_name;
                riskteam.risk_program_group_id = self.programs_type;
            else:
                riskteam = app_model.RiskProgramDetail();
                log.info("add team"); 

                riskteam.description = self.programs_name;
                riskteam.risk_program_group_id = self.programs_type;
                riskteam.save();
            
        except Exception, exception:
            log.info("error : " + str(exception));
            print exception;
            self.message ="fail";
            self.success = False;
            log.info("create risk");
            log.info(kw);
            
        return dict(success=self.success, message = self.message);
    
    
    @expose('json')
    def deletePrograms(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        self.message ="sucess";
        self.success = True;
        try:
            log.info("delete section");
            log.info(kw);
             
            self.programs_id   = self.util.isValue(kw.get('id'));
            self.programs_name = self.util.isValue(kw.get('name'));
            self.programs_type = self.util.isValue(kw.get('type'));
            
            if(self.programs_id is not None):
                log.info("delete section team");
                section = app_model.RiskProgramDetail.getById(self.programs_id);
                section.remove(); 
               
      
         
        except Exception, exception:
            log.info("error : " + str(exception));
            print exception;
            self.message ="fail";
            self.success = False;
            log.info("delete section team");
            log.info(kw);
            
        return dict(success=self.success, message = self.message);
    
    
    @expose('json')
    def saveRiskLevel(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        self.message ="sucess";
        self.success = True;
        try:
            log.info("create Risk Level");
            log.info(kw);
             
            self.id   = self.util.isValue(kw.get('id'));
            self.name = kw.get('name');
            self.type = self.util.isValue(kw.get('type'));
            self.eff = self.util.isValue(kw.get('eff'));
          
            if(self.id is not None):
                log.info("update Risk Level");
                obj = app_model.RiskLevel.getById(self.id);
                log.info( "name : " + str(self.name));
                
                obj.description = self.name;
                obj.effective = self.eff;
                obj.risk_program_group_id = self.type;
                
                if self.type == 1:
                    obj.is_clinical = self.type;
                    obj.is_physical = 0;
                else:
                    obj.is_clinical = self.type;
                    obj.is_physical = 1;
            else:
                obj = app_model.RiskLevel();
                log.info("add Risk Level"); 

                obj.description = self.name;
                obj.effective = self.eff;
                obj.risk_program_group_id = self.type;
                
                if self.type == 1:
                    obj.is_clinical = self.type;
                    obj.is_physical = 0;
                else:
                    obj.is_clinical = self.type;
                    obj.is_physical = 1;
                obj.save();
            
        except Exception, exception:
            log.info("error : " + str(exception));
            print exception;
            self.message ="fail";
            self.success = False;
            log.info("create risk");
            log.info(kw);
            
        return dict(success=self.success, message = self.message);
    
    
    @expose('json')
    def deleteRiskLevel(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        self.message ="sucess";
        self.success = True;
        try:
            log.info("delete risklevel");
            log.info(kw);
             
            self.id   = self.util.isValue(kw.get('id'));
            self.name = self.util.isValue(kw.get('name'));
            self.type = self.util.isValue(kw.get('type'));
            self.eff = self.util.isValue(kw.get('eff'));
            
            if(self.id is not None):
                log.info("delete risklevel");
                obj = app_model.RiskLevel.getById(self.id);
                obj.remove(); 
               
      
         
        except Exception, exception:
            log.info("error : " + str(exception));
            print exception;
            self.message ="fail";
            self.success = False;
            log.info("delete risklevel");
            log.info(kw);
            
        return dict(success=self.success, message = self.message);
    
    @expose('json')
    def saveUser(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        self.message ="sucess";
        self.success = True;
        try:
            log.info("create Risk Level");
            log.info(kw);
             
            self.id   = self.util.isValue(kw.get('id'));
            self.name = self.util.isValue(kw.get('name')); 
            self.email = self.util.isValue(kw.get('email'));
            self.display = self.util.isValue(kw.get('display'));
            self.group_id = self.util.isValue(kw.get('group_id'));
            self.password = self.util.isValue(kw.get('password'));
            self.verify_password = self.util.isValue(kw.get('verify_password'));
          
            if(self.id is not None):
                log.info("update Risk Level");
                obj = app_model.User.getById(self.id);
                
                obj.user_name = self.name;
                obj.email_address = self.email;
                obj.display_name = self.display;
    
                if(self.password is not None and self.verify_password is not None and 
                   self.password == self.verify_password):
                    obj._set_password(self.password);
                    
                
                
                group = app_model.Group.updateUserGroup(self.id,self.group_id);
                log.info("update group_user : " + str(group));
                     
            else:
                
                #check User
                obj = app_model.User.by_user_name(self.name);
                if obj is None:
                    obj = app_model.User.by_email_address(self.email); 
                    if obj is None:            
                        obj = User();
                        log.info("add Risk Level"); 
        
                        obj.user_name = self.name;
                        obj.email_address = self.email;
                        obj.display_name = self.display;
                        if(self.password is not None and self.verify_password is not None and 
                           self.password == self.verify_password):
                            obj._set_password(self.password);
                        
                        obj.save();
                        
                        
                        group = app_model.Group.insertUserGroup(obj.user_id,self.group_id);
                        log.info("insert group_user : " + str(group));
                    else:
                        self.message = "email :" + self.email + " มีในระบบแล้ว";
                        self.success = False;
                else:
                    self.message = "user :" + self.name + " มีในระบบแล้ว";
                    self.success = False;
                
            
        except Exception, exception:
            log.info("error : " + str(exception));
            print exception;
            self.message ="fail";
            self.success = False;
            log.info("create risk");
            log.info(kw);
            
        return dict(success=self.success, message = self.message);
    
    
    @expose('json')
    def deleteUser(self,**kw):
        reload(sys);
        sys.setdefaultencoding("utf-8");
        self.message ="sucess";
        self.success = True;
        try:
            log.info("delete risklevel");
            log.info(kw);
             
            self.id   = self.util.isValue(kw.get('id'));
            self.name = self.util.isValue(kw.get('name')); 
            self.email = self.util.isValue(kw.get('email'));
            self.display = self.util.isValue(kw.get('display'));
            self.group_id = self.util.isValue(kw.get('group_id'));
            self.password = self.util.isValue(kw.get('password'));
            self.verify_password = self.util.isValue(kw.get('verify_password'));
          
            if(self.id is not None):
                log.info("delete User");
                obj = app_model.User.getById(self.id);
                obj.remove();
                log.info("delete User group");
                app_model.Group.removeUserGroup(self.id); 
               
      
         
        except Exception, exception:
            log.info("error : " + str(exception));
            print exception;
            self.message ="fail";
            self.success = False;
            log.info("delete risklevel");
            log.info(kw);
            
        return dict(success=self.success, message = self.message);
    @expose('json')
    def listUser(self,**kw):
        #users = DBSession.query(User).all();
        groups = app_model.DBSession.query(app_model.Group).all();
        self.list = [];
        for group in groups:
            for guser in group.users:
                self.list.append({'id' : guser.user_id ,
                         'name' : guser.user_name,
                         'display' : guser.display_name,
                         'email' : guser.email_address,
                         'group_id' :  group.group_id,
                         'group' : group.group_name
                         }); 
       
        return dict(root = self.list,total=str(len(self.list)));
    
    @expose('json')
    def listGroupUser(self,**kw):
        groups = app_model.DBSession.query(app_model.Group).all();
        self.listgroup = [];
        for group in groups:
            self.listgroup.append({'id' : group.group_id ,
                              'name' :  group.group_name 
                         }); 
       
        return dict(root = self.listgroup,total=str(len(self.listgroup)));
    @expose('comcenter.templates.risk.admin.admin2')
    def admin2(self,**kw):
        
        return dict(page='risk' );
    
    @expose('comcenter.templates.risk.admin.admin3')
    def admin3(self,**kw):
        
        return dict(page='risk' );
    
    @expose('comcenter.templates.risk.admin.admin4')
    def admin4(self,**kw):
        
        return dict(page='risk' );
    