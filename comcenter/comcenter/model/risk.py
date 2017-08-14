# -*- coding: utf-8 -*-
import os
from datetime import datetime
import sys
from repoze.who.config import _LEVELS
try:
    from hashlib import sha1
except ImportError:
    sys.exit('ImportError: No module named hashlib\n'
             'If you are on python2.4 this library is not part of python. '
             'Please install it. Example: easy_install hashlib')

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime, String, Text
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.orm import relation, synonym
from sqlalchemy import *;

from sqlalchemy import schema as saschema 
from comcenter.model import DeclarativeBase, metadata, DBSession
from comcenter.model.auth import User;
#from sqlalchemy.sql.expression import *;
import logging;
import sys;
import copy
from comcenter.controllers.util.utility import *; 
log = logging.getLogger(__name__);

__all__ = ['RiskLevel', 'RiskProgramGroup', 'RiskProgramDetail','RiskStatus', 'RiskSection','RiskTeamType','RiskTeam',
           'RiskManagement','RiskResponsible','UserRiskSection', 'SectionListTeam','Questionnaires'];

class RiskLevel(DeclarativeBase):
    __tablename__ = 'risk_level';
    risk_level_id = Column(Integer, autoincrement=True, primary_key=True);
    description = Column(String(255), unique=True, nullable=False);
    is_clinical = Column(Integer,   nullable=False,  default=0   );
    is_physical = Column(Integer,   nullable=False,  default=0   );
    effective = Column(   Text, nullable=True);
    alert_report = Column( BIT, default = 0);
    
    risk_program_group_id = Column(   Integer,ForeignKey('risk_program_group.risk_program_group_id'), nullable=False, index=True) ;
    risk_program_group  = relation('RiskProgramGroup', backref='risklevelprogramgroup');
    def __init__(self):
        self.risk_level_id = None;
        self.description = None;
        self.is_clinical = 0;
        self.is_physical = 0;
        self.risk_program_group_id =1;
        self.alert_report = 0;
    
    def initData(self):
        self.data = RiskLevel();
        self.data.description = 'A';
        self.data.save();
        
        self.data = RiskLevel();
        self.data.description = 'B';
        self.data.save();
        
        self.data = RiskLevel();
        self.data.description = 'C';
        self.data.save();
        
        self.data = RiskLevel();
        self.data.description = 'D';
        self.data.save();
        
        self.data = RiskLevel();
        self.data.description = 'E';
        self.data.save();
        
        self.data = RiskLevel();
        self.data.description = 'F';
        self.data.save();
        
        self.data = RiskLevel();
        self.data.description = 'G';
        self.data.save();
        
        self.data = RiskLevel();
        self.data.description = 'H';
        self.data.save();
        
        self.data = RiskLevel();
        self.data.description = 'I';
        self.data.save();
    
    def __str__(self):
        return "<RiskLevel : risk_level_id=%s,description=%s,clinical=%s, physical=%s alert_report=%s>"  \
            %(self.risk_level_id, self.description, self.is_clinical, self.is_physical, self.alert_report)    
    def save(self):
        DBSession.add(self); 
        DBSession.flush() ;
    
    def update(self):
        DBSession.update(self);
        
    def remove(self):
        DBSession.delete(self);
        DBSession.flush() ;
    
    @classmethod
    def getById(cls,id):
        return DBSession.query(cls) .get(str(id));
        
    @classmethod
    def listAll(cls):
        return DBSession.query(cls).order_by(cls.description).all();
    
    @classmethod
    def listRiskByClinical(cls):
        return DBSession.query(cls).filter(  cls.is_clinical == 1 ).order_by(cls.description).all();
   
    @classmethod
    def listRiskByPhysical(cls):
        return DBSession.query(cls).filter(  cls.is_physical == 1 ).order_by(cls.description).all();
        
        
class RiskProgramGroup(DeclarativeBase):
    __tablename__ = 'risk_program_group';
    risk_program_group_id = Column(Integer, autoincrement=True, primary_key=True);
    description = Column(String(255), unique=True, nullable=False);
    
    def __init__(self):
        self.risk_program_group_id = None;
        self.description = None;

     
        
    def save(self):
        DBSession.add(self); 
        DBSession.flush() ;
    
    def update(self):
        DBSession.update(self);
        
    def remove(self):
        DBSession.delete(self);
        DBSession.flush() ;
    @classmethod
    def getById(cls,id):
        return DBSession.query(cls) .get(str(id));
    @classmethod
    def listAll(cls):
        return DBSession.query(cls).order_by(cls.risk_program_group_id).all(); 
        
class RiskProgramDetail(DeclarativeBase):
    __tablename__ = 'risk_program_detail';
    risk_program_detail_id = Column(Integer, autoincrement=True, primary_key=True);
    description = Column(String(255), unique=True, nullable=False);
    risk_program_group_id = Column(   Integer,ForeignKey('risk_program_group.risk_program_group_id'), nullable=False, index=True) ;
    risk_program_group  = relation('RiskProgramGroup', backref='riskprogramdetail');
    
    def __init__(self):
        self.risk_program_detail_id = None;
        self.risk_program_group_id = None;
        self.description = None;
    
    def initData(self):
        self.riskProgramGroup = RiskProgramGroup();
        self.riskProgramGroup.description = 'โปรแกรมทางคลินิก';
        self.riskProgramGroup.save();
        
        self.data = RiskProgramDetail();
        self.data.description= 'ภาวะแทรกซ้อน';
        self.data.risk_program_group_id = self.riskProgramGroup.risk_program_group_id;
        self.data.save();
        
        self.data = RiskProgramDetail();
        self.data.description= 'ความผิดพลาดจากการให้บริการ';
        self.data.risk_program_group_id = self.riskProgramGroup.risk_program_group_id;
        self.data.save();
        
        self.data = RiskProgramDetail();
        self.data.description= 'อื่นๆ';
        self.data.risk_program_group_id = self.riskProgramGroup.risk_program_group_id;
        self.data.save();
        
        self.data = RiskProgramDetail();
        self.data.description= 'IC/ปัจจัยที่ก่อให้เกิดการติดเชื้อ';
        self.data.risk_program_group_id = self.riskProgramGroup.risk_program_group_id;
        self.data.save();
        
        self.data = RiskProgramDetail();
        self.data.description= 'ความคลาดเคลื่อนทางยา';
        self.data.risk_program_group_id = self.riskProgramGroup.risk_program_group_id;
        self.data.save();
        
        self.data = RiskProgramDetail();
        self.data.description= 'ความคลาดเคลื่อนทางเวชระเบียน';
        self.data.risk_program_group_id = self.riskProgramGroup.risk_program_group_id;
        self.data.save();
        
        self.data = RiskProgramDetail();
        self.data.description= 'ระบบ  Hosxp software';
        self.data.risk_program_group_id = self.riskProgramGroup.risk_program_group_id;
        self.data.save();
        
        self.data = RiskProgramDetail();
        self.data.description= 'เครื่องมือเวชภัณฑ์ที่เกิ่ยวกับผู้ป่วย';
        self.data.risk_program_group_id = self.riskProgramGroup.risk_program_group_id;
        self.data.save();
        
        self.riskProgramGroup = RiskProgramGroup();
        self.riskProgramGroup.description = 'โปรแกรมทางกายภาพ';
        self.riskProgramGroup.save();
        
        self.data = RiskProgramDetail();
        self.data.description= 'ESB';
        self.data.risk_program_group_id = self.riskProgramGroup.risk_program_group_id;
        self.data.save();
        
        self.data = RiskProgramDetail();
        self.data.description= 'รักษาความปลอกภัย';
        self.data.risk_program_group_id = self.riskProgramGroup.risk_program_group_id;
        self.data.save();
        
        self.data = RiskProgramDetail();
        self.data.description= 'บุคคล';
        self.data.risk_program_group_id = self.riskProgramGroup.risk_program_group_id;
        self.data.save();
        
        self.data = RiskProgramDetail();
        self.data.description= 'OC, Safety';
        self.data.risk_program_group_id = self.riskProgramGroup.risk_program_group_id;
        self.data.save();
        
        self.data = RiskProgramDetail();
        self.data.description= 'เครื่องมือ อุปกรณ์อื่นๆ';
        self.data.risk_program_group_id = self.riskProgramGroup.risk_program_group_id;
        self.data.save();
        
        self.data = RiskProgramDetail();
        self.data.description= 'สิ่งแวดล้อมและอาคารสถานที่';
        self.data.risk_program_group_id = self.riskProgramGroup.risk_program_group_id;
        self.data.save();
        
        self.data = RiskProgramDetail();
        self.data.description= 'สาธารณูปโภค';
        self.data.risk_program_group_id = self.riskProgramGroup.risk_program_group_id;
        self.data.save();
        
        self.data = RiskProgramDetail();
        self.data.description= 'อัคคีภัย';
        self.data.risk_program_group_id = self.riskProgramGroup.risk_program_group_id;
        self.data.save();
        
        self.data = RiskProgramDetail();
        self.data.description= 'การเงิน';
        self.data.risk_program_group_id = self.riskProgramGroup.risk_program_group_id;
        self.data.save();
        
        self.data = RiskProgramDetail();
        self.data.description= 'ในชุมชน';
        self.data.risk_program_group_id = self.riskProgramGroup.risk_program_group_id;
        self.data.save();
        
    def save(self):
        DBSession.add(self); 
        DBSession.flush() ;
    
    def update(self):
        DBSession.update(self);
        
    def remove(self):
        DBSession.delete(self);
        DBSession.flush() ;
    
    @classmethod
    def getById(cls,id):
        return DBSession.query(cls) .get(str(id));
    
    @classmethod
    def listAll(cls):
        return DBSession.query(cls).order_by(cls.risk_program_detail_id).all();

    @classmethod
    def listAllByGroup(cls,group_id):
        return DBSession.query(cls).filter(  cls.risk_program_group_id == str(group_id) ).order_by(cls.risk_program_detail_id).all(); 
        
class RiskStatus(DeclarativeBase):
    __tablename__ = 'risk_status';
    risk_status_id = Column(Integer, autoincrement=True, primary_key=True);
    description = Column(String(255), unique=True, nullable=False);
    
    def __init__(self):
        self.risk_status_id = None;
        self.description = None;
    
    def initData(self):
        self.data = RiskStatus();
        self.data.description = 'รอพิจารณา';
        self.data.save();
        
        self.data = RiskStatus();
        self.data.description = 'รับรายงาน';
        self.data.save();        
        
        self.data = RiskStatus();
        self.data.description = 'นำส่งหน่วยงาน';
        self.data.save();    
        
        self.data = RiskStatus();
        self.data.description = 'แก้ไขและตอบกลับ';
        self.data.save();
        
        self.data = RiskStatus();
        self.data.description = 'สมบูรณ์';
        self.data.save();
    
    def save(self):
        DBSession.add(self); 
        DBSession.flush() ;
    
    def update(self):
        DBSession.update(self);
        
    def remove(self):
        DBSession.delete(self);
        DBSession.flush() ;
        
    @classmethod
    def listAll(cls):
        return DBSession.query(cls).order_by(cls.risk_status_id).all(); 
        
class RiskSection(DeclarativeBase):
    __tablename__ = 'risk_section';
    risk_section_id = Column(Integer, autoincrement=True, primary_key=True);
    description = Column(String(255), unique=True, nullable=False);
    
    def __init__(self):
        self.risk_section_id = None;
        self.description = None;
    
    def initData(self):
        self.value = ['OPD','ER','Ward หญิง', 'Ward ชาย', 'LR', 'OR/Anes', 'เภสัชกรรม+pct round', 'ชันสูตร', 'รังสีวิทยา', 
                      'ทันตกรรม', 'เวชปฎิบัติครอบครัว', 'กายภาพ', 'แพทย์แผยไทย', 'เวชระเบียน', 'Supply', 'ซักฟอก', 'โรงครัว', 
                      'บริหารฯ+การเงิน+ยานฯ+ยาม', 'ประกันสุขภาพ', 'สุขาภิบาลและสิ่งแวดล้อม', 'งานสุขภาพจิต', 'ปชส+ศูนย์ตรวจสุขภาพ', 'การพยาบาลผู้สูงอายุ', 
                      'ส่งเสริมการเรียนรู้', 'โรงผลิตสมุนไพร', 'การพยาบาลเด็ก', 'HHC', 'ENV round', 'audit เวชระเบียน', 'แพทย์/ทบทวน PCT/COPD'];
        for v in self.value:
            self.data = RiskSection();
            self.data.description = v;
            self.data.save();
    
    def save(self):
        DBSession.add(self); 
        DBSession.flush() ;
    
    def update(self):
        DBSession.update(self);
        
    def remove(self):
        DBSession.delete(self);
        DBSession.flush() ;
        
    @classmethod
    def listAll(cls):
        return DBSession.query(cls).order_by(cls.risk_section_id).all();   
    
    @classmethod
    def listBySection(cls,section_id):
        return DBSession.query(cls).filter(  cls.risk_section_id == str(section_id)).order_by(cls.risk_section_id).all();   
    
    @classmethod
    def listBySectionbyId(cls,section_id):
        return DBSession.query(cls).filter(  cls.risk_section_id == str(section_id)).order_by(cls.risk_section_id).first();   
    
        
class RiskTeamType(DeclarativeBase):
    __tablename__ = 'risk_team_type';
    risk_team_type_id = Column(Integer, autoincrement=True, primary_key=True);
    description = Column(String(255), unique=True, nullable=False);
    
    def __init__(self):
        self.risk_team_type_id = None;
        self.description = None;
        
    def save(self):
        DBSession.add(self); 
        DBSession.flush() ;
    
    def update(self):
        DBSession.update(self);
        
    def remove(self):
        DBSession.delete(self);
        DBSession.flush() ;   
    
    
    @classmethod
    def listTeamTypeAll(cls):
        return DBSession.query(cls).order_by(cls.risk_team_type_id).all();
        
class RiskTeam(DeclarativeBase):
    __tablename__ = 'risk_team';
    risk_team_id = Column(Integer, autoincrement=True, primary_key=True);
    description = Column(String(255), unique=True, nullable=False);
    risk_team_type_id = Column(   Integer,ForeignKey('risk_team_type.risk_team_type_id'), nullable=False, index=True) ;
    risk_team_type  = relation('RiskTeamType', backref='riskteam');
    active  =  Column(String(1) , nullable=False,default =1);
    def __init__(self):
        self.risk_team_id = None;
        self.description = None;
        self.active = '1';
    
    def initData(self):
        self.value = ['OPD','ER','Ward หญิง', 'Ward ชาย', 'LR', 'OR/Anes', 'เภสัชกรรม', 'ชันสูตร', 'รังสีวิทยา', 
                      'ทันตกรรม', 'เวชปฎิบัติครอบครัว', 'กายภาพ', 'แพทย์แผยไทย', 'เวชระเบียน', 'Supply', 'ซักฟอก', 'โรงครัว', 
                      'บริหารฯ+การเงิน+ยานฯ+ยาม', 'ประกันสุขภาพ', 'สุขาภิบาลและสิ่งแวดล้อม', 'งานสุขภาพจิต', 'ปชส+ศูนย์ตรวจสุขภาพ+IT', 'การพยาบาลผู้สูงอายุ', 
                      'งานส่งเสริมการเรียนรู้', 'โรงผลิตสมุนไพร', 'การพยาบาลเด็ก+ศูนย์เด็ก', 'PCU'];
        
        self.value1 = ['PCT', 'SSD', 'IC', 'ENV', 'HRM', 'NUR', 'IM', 'MED/พยาบาลเวชฯ', 'Ptc', 'ลูกเกิดรอด/สายใยรัก', '5 ส.', 'HHC', 'ศูนย์เครื่องมือแพทย์', 'RM', 'คปสอ.'];
        
        self.teamType = RiskTeamType();
        self.teamType.description = 'หน่วยงาน';
        self.teamType.save();
        
        
        for v in self.value:
            self.data = RiskTeam();
            self.data.description = v;
            self.data.risk_team_type_id =self.teamType.risk_team_type_id; 
            self.data.save();
            
        self.teamType = RiskTeamType();
        self.teamType.description = 'ทีมคร่อม';
        self.teamType.save();
        
        
        for v in self.value1:
            self.data = RiskTeam();
            self.data.description = v;
            self.data.risk_team_type_id =self.teamType.risk_team_type_id; 
            self.data.save();
            
        
    def save(self):
        DBSession.add(self); 
        DBSession.flush() ;
    
    def update(self):
        DBSession.update(self);
        
    def remove(self):
        DBSession.delete(self);
        DBSession.flush() ;    
    
    @classmethod
    def getById(cls,id):
        return DBSession.query(cls) .get(str(id)); 
    

    @classmethod
    def listTeamByActive(cls,team_type=None):
        if(team_type):
            return DBSession.query(cls).filter(  and_(cls.risk_team_type_id == str(team_type), cls.active == str('1') ) ).order_by(cls.risk_team_id).all();
        
        return DBSession.query(cls).order_by(cls.risk_team_id).all();
    
    
    @classmethod
    def listTeam(cls,team_type=None):
        if(team_type):
            return DBSession.query(cls).filter(  cls.risk_team_type_id == str(team_type)).order_by(cls.risk_team_id).all();
        
        return DBSession.query(cls).order_by(cls.risk_team_id).all();
    
    @classmethod
    def listTeamCrom(cls):
        return DBSession.query(cls).filter(cls.risk_team_type_id == str(2)).all();
    
    @classmethod
    def listTeamAll(cls):
        return DBSession.query(cls).all();
    
class RiskManagement(DeclarativeBase):
    __tablename__ = 'risk_management';
    risk_management_id = Column(Integer, autoincrement=True, primary_key=True);
    detail = Column(   Text, nullable=False);
    
    solution = Column(   Text, nullable=False);
    
    risk_level_id  = Column(   Integer,ForeignKey('risk_level.risk_level_id'), nullable=False, index=True) ;
    risk_level   = relation('RiskLevel', backref='riskmanagement');
    
    risk_section_id = Column(   Integer,ForeignKey('risk_section.risk_section_id'), nullable=False, index=True) ;
    risk_section = relation('RiskSection', backref='riskmanagement');
    
    risk_program_detail_id = Column(   Integer,ForeignKey('risk_program_detail.risk_program_detail_id'), nullable=False, index=True) ;
    risk_program_detail = relation('RiskProgramDetail', backref='riskmanagement');
    
    risk_status_id = Column(   Integer,ForeignKey('risk_status.risk_status_id'), nullable=False, index=True) ;
    risk_status = relation('RiskStatus', backref='riskmanagement');
    
    report_date =  Column(DateTime, nullable=False, default=datetime.now);
    create_date =  Column(DateTime, nullable=False, default=datetime.now);
    active =  Column(String(1) , nullable=False,default =1);
    
    def __init__(self):
        self.risk_management_id = None;
        self.detail = None;
        self.risk_level_id = 0;
        self.risk_section_id = 0;
        self.risk_program_detail_id = 0;
        self.risk_status_id = 0;
        self.report_date =  datetime.now();
        self.create_date =  datetime.now();
        self.active = '1';
        
    def save(self):
        DBSession.add(self); 
        DBSession.flush() ;
    
    def update(self):
        DBSession.update(self);
        
    def remove(self):
        DBSession.delete(self);
        DBSession.flush() ;   
    @classmethod
    def getById(cls,id):
        return DBSession.query(cls) .get(str(id)); 
    
    @classmethod
    def checkResponsible(cls,riskId):
        sql = text("""select risk_responsible.* 
                from risk_management inner JOIN risk_responsible on risk_management.risk_management_id = risk_responsible.risk_management_id 
            WHERE
                risk_management.risk_status_id  in (3, 4)
                and risk_management.risk_management_id = """ + riskId  + """
                and  risk_responsible.detail = '' """);
        result = DBSession.execute(sql);
        count = 0;
        for row in result:
            count = count +1;
            #risk_responsible_id = row['risk_responsible_id'];
        
        if(count>0):
            return  False;
        return True;
        
    @classmethod
    def showRiskRespManage(cls,startDate, stopDate, riskSection, riskProgramGroup, riskStatus,riskProgramDetail,riskId):
        sql =" and  1=1 ";
        
        if (startDate and stopDate) :
            sql = sql + "and DATE_FORMAT(risk_management.report_date ,'%Y-%m-%d')  between '" + startDate + "' and '" + stopDate + "'  ";
        else: 
            if(startDate ):
                sql = sql + "and risk_management.report_date >= '" + startDate + "'";
            else:
                if(stopDate):
                    sql = sql + "and risk_management.report_date <= '" + stopDate + "'";
            
        
            
        if(riskSection):
            sql = sql + "and section_list_team.risk_section_id  = "+ riskSection;
        if(riskProgramGroup):
            sql = sql + " and risk_program_group.risk_program_group_id = "+ riskProgramGroup;
        #if(riskStatus):
        
        sql = sql + " and risk_management.risk_status_id >= 3 " ;#+ riskStatus;
        
        if(riskProgramDetail):
            sql = sql + " and risk_management.risk_program_detail_id = "+ riskProgramDetail;
        
        if(riskId):
            sql = sql + " and risk_management.risk_management_id = "+ riskId;
        
        
        sql = text("""select
                            risk_responsible.risk_responsible_id  ,
                            risk_management.risk_management_id,
                            risk_management.detail as risk_detail,
                            risk_management.solution as risk_solution,
                            risk_management.report_date as report_date,
                            risk_level.risk_level_id,
                            risk_level.description as risk_level,
                            CONCAT(risk_level.description,' ' ,risk_level.effective) as level_desc ,
                            risk_section.risk_section_id,
                            risk_section.description as risk_section,
                            risk_program_detail.risk_program_detail_id,
                            risk_program_detail.description as risk_program_detail,
                            risk_responsible.detail ,
                            risk_responsible.risk_team_id,
                            risk_program_group.risk_program_group_id,
                            risk_program_group.description as risk_program_group,
                           
                            risk_management.risk_status_id 
                             
                            
                        FROM
                        risk_management INNER JOIN risk_responsible ON risk_management.risk_management_id = risk_responsible.risk_management_id
                        INNER JOIN risk_section on risk_management.risk_section_id = risk_section.risk_section_id
                        INNER JOIN risk_level on risk_level.risk_level_id = risk_management.risk_level_id
                        INNER JOIN risk_program_detail on risk_program_detail.risk_program_detail_id = risk_management.risk_program_detail_id
                        INNER JOIN risk_program_group on risk_program_group.risk_program_group_id = risk_program_detail.risk_program_group_id
                        LEFT JOIN section_list_team on section_list_team.risk_team_id = risk_responsible.risk_team_id  
                        
                        where risk_management.active = 1    """ + sql  + """ GROUP BY
                            risk_management.risk_management_id,
                            risk_management.detail  ,
                            risk_level.risk_level_id,
                            risk_level.description  ,
                            risk_section.risk_section_id,
                            risk_section.description  ,
                            risk_program_detail.risk_program_detail_id,
                            risk_program_detail.description   ,
                            risk_responsible.detail ,
                            risk_responsible.risk_team_id,
                           risk_management.risk_status_id,
                           risk_responsible.risk_responsible_id  """ );
        #and LENGTH( TRIM(risk_responsible.detail)) =0
        result = DBSession.execute(sql);
        
        print "test";
        list = [];
        for row in result:
            section_team = RiskResponsible.getSectionTeam('1', row['risk_management_id'],riskSection);
            crom_team =  RiskResponsible.getSectionTeam('2', row['risk_management_id'],riskSection);
         
            list.append({ 'risk_management_id':row['risk_management_id'], 
                           'report_date':row['report_date'], 
                          'risk_detail' :row['detail'] ,
                          'risk_solution' : row['risk_solution'],
                          'detail' : row['risk_detail'],
                          'risk_team_id' : row['risk_team_id'],
                           'risk_level_id' :row['risk_level_id'] ,
                           'level_desc' : row ['level_desc'],
                          'risk_section_id' :row['risk_section_id'] ,                        
                          'risk_program_group_id' : row['risk_program_group_id'],                        
                          'risk_level' :row['risk_level'],
                          'risk_section' :row['risk_section'],
                          'risk_program_detail' :row['risk_program_detail'],  
                          'risk_program_group' :row['risk_program_group'],  
                          'risk_program_detail_id':row['risk_program_detail_id'] ,
                         'risk_status_id' :row['risk_status_id'],
                          'crom_team' : crom_team,
                          'section_team' : section_team ,
                          'risk_responsible_id' :  row['risk_responsible_id']
                        });
           
        return list; 
    @classmethod    
    def showRiskManage(cls,startDate, stopDate, riskSection, riskProgramGroup, riskStatus,riskProgramDetail,riskId):
        
        sql =" and  1=1 ";
        
      ##  if(startDate ):
      ##      sql = sql + "and risk_management.report_date >= '" + startDate + "'";
      ##        if(stopDate):
      ##            sql = sql + "and risk_management.report_date <= '" + stopDate + "'";
            
        if (startDate and stopDate) :
            sql = sql + "and DATE_FORMAT(risk_management.report_date ,'%Y-%m-%d')  between '" + startDate + "' and '" + stopDate + "'  ";
        else: 
            if(startDate ):
                sql = sql + "and risk_management.report_date >= '" + startDate + "'";
            else:
                if(stopDate):
                    sql = sql + "and risk_management.report_date <= '" + stopDate + "'";   
            
        if(riskSection):
            sql = sql + " and risk_management.risk_section_id = "+ riskSection;
        if(riskProgramGroup):
            sql = sql + " and risk_program_group.risk_program_group_id = "+ riskProgramGroup;
        if(riskStatus):
            sql = sql + " and risk_management.risk_status_id = "+ riskStatus;
        if(riskProgramDetail):
            sql = sql + " and risk_management.risk_program_detail_id = "+ riskProgramDetail;
        
        if(riskId):
            sql = sql + " and risk_management.risk_management_id = "+ riskId;
        
        
        sql = text("""select risk_management.risk_management_id,risk_management.detail,risk_management.solution, risk_management.risk_level_id,risk_management.risk_section_id,
                        risk_management.risk_status_id, risk_management.report_date, risk_management.create_date,
                        risk_level.description as risk_level , CONCAT(risk_level.description,' ' ,risk_level.effective) as level_desc ,  risk_section.description as risk_section, risk_program_detail.description as risk_program_detail,
                        risk_program_group.description as risk_program_group, risk_program_detail.risk_program_detail_id, risk_program_group.risk_program_group_id,risk_status.description as risk_status
                        from risk_management INNER JOIN risk_level on risk_management.risk_level_id = risk_level.risk_level_id
                                INNER JOIN risk_section on risk_management.risk_section_id = risk_section.risk_section_id
                                INNER JOIN risk_program_detail on risk_management.risk_program_detail_id = risk_program_detail.risk_program_detail_id
                                INNER JOIN risk_program_group on risk_program_group.risk_program_group_id = risk_program_detail.risk_program_group_id
                                INNER JOIN risk_status on risk_management.risk_status_id = risk_status.risk_status_id
                        where risk_management.active = 1 """ + sql );
        
        result = DBSession.execute(sql);
        
        list = [];
        for row in result:
            
            section_team = RiskResponsible.getSectionTeamArray('1', row['risk_management_id']);
            crom_team =  RiskResponsible.getSectionTeamArray('2', row['risk_management_id']);
            list.append({ 'risk_management_id':row['risk_management_id'], 
                          'detail' :row['detail'] ,
                          'risk_solution' : row['solution'],
                           'risk_level_id' :row['risk_level_id'] ,
                          'risk_section_id' :row['risk_section_id'] ,
                          'risk_status_id' :row['risk_status_id'],
                          'risk_program_group_id' : row['risk_program_group_id'],
                          'report_date' :row['report_date'],
                          'create_date' :row['create_date'],
                          'risk_level' :row['risk_level'],
                          'level_desc' : row['level_desc'],
                          'risk_section' :row['risk_section'],
                          'risk_program_detail' :row['risk_program_detail'],  
                          'risk_program_group' :row['risk_program_group'],  
                          'risk_program_detail_id':row['risk_program_detail_id'],
                          'risk_status' :row['risk_status']  ,
                          'crom_team' : crom_team,
                          'section_team' : section_team 
                        });
           
        return list; 
    
    @classmethod    
    def showSumSectionReport(cls,startDate, stopDate):
        sql = "";
        list = [];
        if(startDate and stopDate):
            sql = " and risk_management.report_date BETWEEN '" + startDate + "' and '" + stopDate + "'";
        
        
            sql = text("""select risk_section.description ,COUNT(risk_management.risk_management_id) as count
                            from risk_management LEFT JOIN risk_section on risk_management.risk_section_id = risk_section.risk_section_id
                            where risk_management.active =1
                                """ + sql +"""
                            GROUP BY
                                risk_section.description """);
            result = DBSession.execute(sql);
            
            for row in result:
                list.append({ 'section':row['description'], 'count':row['count']});
            
            return list;
        
    @classmethod
    def showProgramClinicReport(cls,startDate, stopDate,pro_type):
        sql = "";
        list = [];
        if(startDate and stopDate and pro_type):
           
            sql = "and risk_management.report_date BETWEEN '" + startDate + "' and '" + stopDate + "'";
            
            if(pro_type == 1):
                sql = text("""select 
                                risk_program_detail.description,
                            
                                IFNULL(program.A,0) as A,
                                IFNULL(program.B,0) as B,
                                IFNULL(program.C,0) as C,
                                IFNULL(program.D,0) as D,
                                IFNULL(program.E,0) as E,
                                IFNULL(program.F,0) as F,
                                IFNULL(program.G,0) as G,
                                IFNULL(program.H,0) as H,
                                IFNULL(program.I,0) as I
                            FROM
                            risk_program_detail left join (
                            select 
                             risk_program_detail.risk_program_detail_id,
                             risk_program_detail.description ,
                             sum(case when  risk_level.description = 'A' then 1 ELSE 0 end) as A,
                             sum(case when  risk_level.description = 'B' then 1 ELSE 0 end) as B,
                             sum(case when  risk_level.description = 'C' then 1 ELSE 0 end) as C,
                             sum(case when  risk_level.description = 'D' then 1 ELSE 0 end) as D,
                             sum(case when  risk_level.description = 'E' then 1 ELSE 0 end) as E,
                             sum(case when  risk_level.description = 'F' then 1 ELSE 0 end) as F,
                             sum(case when  risk_level.description = 'G' then 1 ELSE 0 end) as G,
                             sum(case when  risk_level.description = 'H' then 1 ELSE 0 end) as H,
                             sum(case when  risk_level.description = 'I' then 1 ELSE 0 end) as I
                            from 
                                -- risk_program_detail LEFT JOIN risk_management on risk_management.risk_program_detail_id = risk_program_detail.risk_program_detail_id
                                risk_management INNER JOIN risk_program_detail on risk_management.risk_program_detail_id = risk_program_detail.risk_program_detail_id
                                LEFT JOIN risk_level on risk_level.risk_level_id = risk_management.risk_level_id
                            where 
                                risk_program_detail.risk_program_group_id = """+str(pro_type) +"""
                                """+ sql+ """
                            GROUP BY
                                 risk_program_detail.risk_program_detail_id
                            ) program on risk_program_detail.risk_program_detail_id =  program.risk_program_detail_id
                            where 
                                risk_program_detail.risk_program_group_id = """+str(pro_type) +"""
                            GROUP BY 
                                risk_program_detail.description
                            order by
                                risk_program_detail.risk_program_detail_id
                              """);
                result = DBSession.execute(sql);
                total = 0;
                for row in result:
                    total = 0;
                    total = row['A'] + row['B']+row['C']+row['D']+row['E']+row['F']+row['G']+row['H']+row['I'];
                    list.append({ 'description':row['description'], 'A':row['A'], 'B':row['B'], 'C':row['C'], 
                                            'D':row['D'], 'E':row['E'], 'F':row['F'], 'G':row['G'], 
                                            'G':row['G'], 'H':row['H'] , 'I':row['I'],"total":total});
            
            else:
                sql = text("""select 
                                risk_program_detail.description,
                            
                                IFNULL(program.0,0) as A,
                                IFNULL(program.1,0) as B,
                                IFNULL(program.2,0) as C,
                                IFNULL(program.3,0) as D
                            FROM
                            risk_program_detail left join (
                            select 
                             risk_program_detail.risk_program_detail_id,
                             risk_program_detail.description ,
                             sum(case when  risk_level.description = '0' then 1 ELSE 0 end) as '0',
                             sum(case when  risk_level.description = '1' then 1 ELSE 0 end) as '1',
                             sum(case when  risk_level.description = '2' then 1 ELSE 0 end) as '2',
                             sum(case when  risk_level.description = '3' then 1 ELSE 0 end) as '3' 
                            from 
                                -- risk_program_detail LEFT JOIN risk_management on risk_management.risk_program_detail_id = risk_program_detail.risk_program_detail_id
                                risk_management INNER JOIN risk_program_detail on risk_management.risk_program_detail_id = risk_program_detail.risk_program_detail_id
                                LEFT JOIN risk_level on risk_level.risk_level_id = risk_management.risk_level_id
                            where 
                                risk_program_detail.risk_program_group_id = """+str(pro_type) +"""
                                """+ sql+ """
                            GROUP BY
                                 risk_program_detail.risk_program_detail_id
                            ) program on risk_program_detail.risk_program_detail_id =  program.risk_program_detail_id
                            where 
                                risk_program_detail.risk_program_group_id = """+str(pro_type) +"""
                            GROUP BY 
                                risk_program_detail.description
                            order by
                                risk_program_detail.risk_program_detail_id
                              """);
                result = DBSession.execute(sql);
                total = 0;
                for row in result:
                    total = 0;
                    total = row['A'] + row['B']+row['C']+row['D'] ;
                    list.append({ 'description':row['description'], 'A':row['A'], 'B':row['B'], 'C':row['C'], 'D':row['D'] ,"total":total});
                                            
            return list;
    
    @classmethod
    def listRiskResponseByUser(cls,user):
        
        sql = text("""
                    select 
                        risk_management.risk_management_id,
                        risk_management.detail as "risk_detail",
                        risk_responsible.risk_responsible_id,
                        risk_responsible.detail as "ans"
                     
                    from 
                        tg_user INNER JOIN user_risk_section on tg_user.user_id = user_risk_section.user_id
                        INNER JOIN section_list_team on user_risk_section.risk_section_id = section_list_team.risk_section_id
                        INNER JOIN risk_responsible on section_list_team.risk_team_id = risk_responsible.risk_team_id
                        INNER JOIN risk_management on risk_responsible.risk_management_id = risk_management.risk_management_id
                    WHERE
                        tg_user.user_name = '""" + user + """'
                        and risk_responsible.detail = ''
                    GROUP BY
                        risk_management.risk_management_id,
                        risk_management.detail  ,
                        risk_responsible.risk_responsible_id,
                        risk_responsible.detail
                """); 
        result = DBSession.execute(sql);
        list= [];
        row_record = 1;
        for row in result:
            list.append({'row':row_record, 'risk_management_id':row['risk_management_id'], 'risk_detail':row['risk_detail'], 'risk_responsible_id':row['risk_responsible_id'], 'ans':row['ans'] });
            row_record = row_record +1;
        return list;
           
    @classmethod
    def listRiskPriority10(cls,startDate, stopDate,limit =None):
        sql = "";
        list = [];
        if(startDate and stopDate):
            limitData = " "  ;    
            if limit :
                limitData = " limit " + str (limit );
           
            sql = "and risk_management.report_date BETWEEN '" + startDate + "' and '" + stopDate + "'";
        
            sql = text("""select 
                            risk_management.risk_management_id,
                            risk_management.detail,
                            risk_management.solution,
                            risk_level.description as level,
                            risk_program_detail.description as pro,
                            risk_section.description as reporter,
                           risk_management.report_date 
                        from risk_management 
                            INNER JOIN risk_level on risk_management.risk_level_id = risk_level.risk_level_id
                            INNER JOIN risk_program_detail on risk_management.risk_program_detail_id = risk_program_detail.risk_program_detail_id
                            INNER JOIN risk_section on risk_management.risk_section_id = risk_section.risk_section_id
                        WHERE    
                            risk_management.active = 1
                            and risk_program_detail.risk_program_group_id = 1
                            """ + sql + """
                        ORDER BY
                            risk_level.description DESC  """ + limitData   );
            result = DBSession.execute(sql);
            total = 0;
            row_record = 1;
            
            for row in result:
                responsible = RiskResponsible.listByRiskManage(row['risk_management_id'])
                
                data = {'row':row_record,'risk_id':row['risk_management_id'], 'detail':row['detail'],'risk_solution':row['solution'], 'level':row['level'], 'pro':row['pro'], 'reporter':row['reporter'] ,'report_date' : row['report_date'],
                        'responsible' : []}
                value = []
                for resp in responsible:
                    value.append(resp.getResp(row['report_date']) );
                    
                data['responsible'] = value
                
                list.append(data);
                row_record = row_record +1;
            return list;
    
    
         
    @classmethod
    def listRiskPriority10Physic(cls,startDate, stopDate,limit =None):
        sql = "";
        list = [];
        if(startDate and stopDate):
            
            limitData = " "  ;    
            if limit :
                limitData = " limit " + str (limit );
            
                
            sql = "and risk_management.report_date BETWEEN '" + startDate + "' and '" + stopDate + "'";
        
            sql = text("""select 
                            risk_management.risk_management_id,
                            risk_management.detail,
                            risk_management.solution,
                            risk_level.description as level,
                            risk_program_detail.description as pro,
                            risk_section.description as reporter,
                            risk_management.report_date 
                        from risk_management 
                            INNER JOIN risk_level on risk_management.risk_level_id = risk_level.risk_level_id
                            INNER JOIN risk_program_detail on risk_management.risk_program_detail_id = risk_program_detail.risk_program_detail_id
                            INNER JOIN risk_section on risk_management.risk_section_id = risk_section.risk_section_id
                        WHERE    
                            risk_management.active = 1
                            and risk_program_detail.risk_program_group_id = 2
                            """ + sql + """
                        ORDER BY
                            risk_level.description DESC """ + limitData  );
            result = DBSession.execute(sql);
            total = 0;
            row_record = 1;
            for row in result:
                responsible = RiskResponsible.listByRiskManage(row['risk_management_id'])
                data = {'row':row_record,'risk_id':row['risk_management_id'], 'detail':row['detail'],
                        'risk_solution':row['solution'], 'level':row['level'], 'pro':row['pro'], 
                        'reporter':row['reporter'] ,'report_date' : row['report_date'],
                        'responsible' : []}
                value = []
                for resp in responsible:
                    value.append(resp.getResp(row['report_date']) );
                
                data['responsible'] = value
                list.append(data);
                row_record = row_record +1;
            return list;
        
    @classmethod
    def listSectionReport(cls,startDate, stopDate) :
        sql = "";
        list = [];
        if(startDate and stopDate):
           
            sql = "and risk_management.report_date BETWEEN '" + startDate + "' and '" + stopDate + "'";
            #sql = "and risk_management.create_date BETWEEN '" + startDate + "' and '" + stopDate + "'";
        
            sql = text("""select 
                            risk_section.description,
                            IFNULL(section_month.month1,0) as month1,
                            IFNULL(section_month.month2,0) as month2,
                            IFNULL(section_month.month3,0) as month3,
                            IFNULL(section_month.month4,0) as month4,
                            IFNULL(section_month.month5,0) as month5,
                            IFNULL(section_month.month6,0) as month6,
                            IFNULL(section_month.month7,0) as month7,
                            IFNULL(section_month.month8,0) as month8,
                            IFNULL(section_month.month9,0) as month9,
                            IFNULL(section_month.month10,0) as month10,
                            IFNULL(section_month.month11,0) as month11,
                            IFNULL(section_month.month12,0) as month12
                        FROM
                            risk_section LEFT JOIN (
                                select
                                    risk_section.risk_section_id as section_id,
                                    sum(case when  MONTH( risk_management.report_date ) = 1 then 1 else 0 end) as month1,
                                    sum(case when  MONTH( risk_management.report_date ) = 2 then 1 else 0 end )as month2,
                                    sum(case when  MONTH( risk_management.report_date ) = 3 then 1 else 0 end) as month3,
                                    sum(case when  MONTH( risk_management.report_date ) = 4 then 1 else 0 end) as month4,
                                    sum(case when  MONTH( risk_management.report_date ) = 5 then 1 else 0 end) as month5,
                                    sum(case when  MONTH( risk_management.report_date ) = 6 then 1 else 0 end) as month6,
                                    sum(case when  MONTH( risk_management.report_date ) = 7 then 1 else 0 end) as month7,
                                    sum(case when  MONTH( risk_management.report_date ) = 8 then 1 else 0 end) as month8,
                                    sum(case when  MONTH( risk_management.report_date ) = 9 then 1 else 0 end) as month9,
                                    sum(case when  MONTH( risk_management.report_date ) = 10 then 1 else 0 end) as month10,
                                    sum(case when  MONTH( risk_management.report_date ) = 11 then 1 else 0 end) as month11,
                                    sum(case when  MONTH( risk_management.report_date ) = 12 then 1 else 0 end) as month12
                                from 
                                    risk_management 
                                    INNER JOIN risk_section on risk_management.risk_section_id = risk_section.risk_section_id
                                WHERE
                                    risk_management.active = 1
                                    """ + sql + """
                                GROUP BY 
                                    risk_section.risk_section_id
                         ) section_month on  risk_section.risk_section_id = section_month.section_id
                        ORDER BY
                            risk_section.risk_section_id


                          """);
            result = DBSession.execute(sql);
            total = 0;
            row_record = 1;
            total =0
            for row in result:
                
                total = row['month1'] + row['month2'] + row['month3'] + row['month4'] +  row['month5'] + row['month6'] + row['month7'] + row['month8']+  row['month9'] + row['month10'] + row['month11'] + row['month12'];
                list.append({'row':row_record, 'description':row['description'], 
                               'month1':row['month1'],'month2':row['month2'],
                               'month3':row['month3'],'month4':row['month4'],
                               'month5':row['month5'],'month6':row['month6'],
                               'month7':row['month7'],'month8':row['month8'],
                               'month9':row['month9'],'month10':row['month10'],
                               'month11':row['month11'],'month12':row['month12'],'total':total});
                row_record = row_record +1;
            return list;
            
    @classmethod
    def listSectionReported(cls,startDate, stopDate) :
        sql = "";
        list = [];
        if(startDate and stopDate):
           
            sql = "  risk_management.report_date BETWEEN '" + startDate + "' and '" + stopDate + "'";
           
            #new report              
            sql = text("""
                        select 
                            risk_team.risk_team_id,
                            risk_team.description ,
                            sum(case when LENGTH( TRIM( risk_responsible.detail) ) then 1 else 0 end ) as reported,
                            sum(case when LENGTH( TRIM( risk_responsible.detail) ) then 0 else 1 end ) as not_reported
                        
                        from 
                            risk_responsible
                            inner join risk_team on risk_responsible.risk_team_id = risk_team.risk_team_id
                            INNER JOIN risk_management on risk_management.risk_management_id = risk_responsible.risk_management_id
                        WHERE    
                                """ + sql + """
                        GROUP BY
                            risk_team.risk_team_id,
                            risk_team.description
                          """);

                          
            result = DBSession.execute(sql);
            total =0;
            for row in result:
                total = row['reported'] + row['not_reported'] ;
                list.append({  'risk_team_id':row['risk_team_id'], 
                               'description':row['description'],'reported':row['reported'],
                               'not_reported':row['not_reported'],'total':total });
                 
            return list;
        
    @classmethod
    def showRiskRespTeamCromManage(cls, riskTeam,startDate, stopDate):
        sql =" and  1=1 ";
        
        if (startDate and stopDate) :
            sql = sql + " and DATE_FORMAT(risk_management.report_date ,'%Y-%m-%d')  between '" + str(startDate) + "' and '" + str(stopDate) + "'  ";
        else: 
            if(startDate ):
                sql = sql + " and risk_management.report_date >= '" + startDate + "'";
            else:
                if(stopDate):
                    sql = sql + " and risk_management.report_date <= '" + stopDate + "'";
        
        if(riskTeam):
            sql = sql + " and risk_team.risk_team_id = " + str(riskTeam)     ;
            
        
        sql = text("""
                            select 
                                risk_responsible.risk_management_id as  risk_id,
                                risk_management.detail as risk_detail,
                                risk_management.solution as risk_solution,
                                risk_management.report_date,
                                risk_section.description as report 
                                from 
                                    risk_management  LEFT OUTER JOIN risk_responsible on risk_responsible.risk_management_id = risk_management.risk_management_id
                                    LEFT OUTER JOIN risk_section on risk_section.risk_section_id = risk_management.risk_section_id     
                                    LEFT OUTER JOIN risk_team on risk_team.risk_team_id = risk_responsible.risk_team_id
                                where 
                                     risk_management.active = 1 AND     risk_team.risk_team_type_id = 2
                                    """ + sql  + """  
                        ORDER BY 
                    risk_management.report_date
                                     """ );
        
        result = DBSession.execute(sql);    
        
        list = [];
        for row in result:
            risk_id = row['risk_id'];
            #row['risk_detail'];
            #row['report_date'];
            #row['report'];
            
            responseTeam = RiskResponsible.getResultTeamByRiskId(  risk_id   );
            
            
            list.append({ 'risk_management_id':row['risk_id'], 
                                'risk_detail' :row['risk_detail'],
                                'risk_solution':row['risk_solution'],
                                'report_date' : row['report_date'],
                                'report' : row['report'] ,
                                'response' : responseTeam                                
                                }); 
         
            
        return list; 
    
    @classmethod    
    def showDetailReportedByMonth(cls,monthInYear):
        sql = "";
        list = [];
        if(monthInYear ):
            sql = " and risk_management.report_date like '" + monthInYear + "' " ;
        
        
            sql = text("""   select  risk_management.risk_management_id  as risk_id,
                                risk_management.detail as risk_detail ,
                                risk_management.solution as risk_solution,
                                risk_section.description as risk_section,
                                risk_management.report_date
                            from risk_management INNER   JOIN risk_section on risk_management.risk_section_id = risk_section.risk_section_id
                            where risk_management.active =1
                                """ + sql +"""
                            ORDER BY
                                report_date DESC """);
            result = DBSession.execute(sql);
            
            for row in result:
                list.append({ 'risk_management_id':row['risk_id']
                                    , 'risk_detail':row['risk_detail']
                                    , 'risk_solution':row['risk_solution']
                                    , 'risk_section':row['risk_section']  
                                    , 'report_date':row['report_date']
                                    });
            
            return list;
    
    @classmethod
    def listResponsibleInTime(cls, risk_team_type, risk_program, startDate, stopDate):
        
        program = []      
        if risk_program == 1:  
            program = RiskLevel.listRiskByPhysical()
        else:
            program = RiskLevel.listRiskByClinical()
        
        d = dict()
        for p in program:
            d[p.description] =   dict(total=0,within=0,percent=0.00)
        
        
        sql = text("""
            select
                
                risk_team.risk_team_id,
                risk_team.description as team
                , risk_level.description
            ,CASE WHEN (TRIM(COALESCE(risk_responsible.detail, '')) = '' ) THEN
                -1 ELSE DATEDIFF(risk_responsible.report_date, risk_management.report_date) END as dif_date_value
             , risk_responsible_intime.criteria
             , risk_responsible_intime.value
            from 
                risk_responsible LEFT JOIN risk_management on risk_responsible.risk_management_id = risk_management.risk_management_id
                LEFT JOIN risk_team on (risk_team.risk_team_id = risk_responsible.risk_team_id )
            LEFT JOIN risk_level on risk_management.risk_level_id = risk_level.risk_level_id
            LEFT JOIN risk_responsible_intime on (risk_responsible_intime.risk_level_id = risk_level.risk_level_id and risk_responsible_intime.active = 1)
            WHERE
                risk_management.report_date BETWEEN :startDate and :stopDate
            and risk_level.is_physical = :riskProgram
            and risk_team.risk_team_type_id = :riskTeamType
            and risk_management.risk_status_id >= 3
            -- and risk_team.risk_team_id in( 43,44)
            ORDER BY risk_team_id
        """)
        #sql.bindparams(x="m", y="z")
        result = DBSession.execute(sql,{'riskProgram':risk_program, 
                                   'riskTeamType':risk_team_type,
                                   'startDate' : startDate,
                                   'stopDate' : stopDate} )#.fetchall()
        data= dict()
        util = Utility();
        
     
        for row in result:
            team = data.get(row[0])            
            if team is None:
                team = {'team_name' : row[1], 'levels': copy.deepcopy(d), 'id':row[0] }
                
                level = {'total' : 1, 'within' : 0, 'percent':0}
                #check within
                if( row[3] >= 0 and util.checkCriteria(int(row[3]), row[4], int(row[5])) ):
                    level['within'] +=1
                #check percent
                level['percent'] =  float("{0:.2f}".format( int(level['within']) * 100.0 / float(level['total']) ))
                
                team['levels'][row[2]] =   level 
                #team[row[2]] =   level 
                    
            else:
                level = team['levels'].get(row[2])
                #check total
                if level is None:
                    level = {'total' : 1, 'within' : 0, 'percent':0}
                else:
                    level['total'] +=1 
                
                #check within
                print "row[0] = %s, row[1] = %s, row[2] = %s, row[3] = %s, row[4] = %s, row[5] = %s, " %(row[0],row[1],row[2],row[3], row[4], row[5])
                if( row[3] >= 0 and util.checkCriteria(int(row[3]), row[4], int(row[5])) ):
                    level['within'] +=1    
                #check percent
                level['percent'] = float("{0:.2f}".format( int(level['within']) * 100.0 / float(level['total']) ))
                
                team['levels'][row[2]] =   level     
                #team[row[2]] = level
            
            data[row[0]] =  team
        
        riskSectionTeam = RiskTeam.listTeam(risk_team_type);
        index = 1
        for riskteam in riskSectionTeam:
           
            team = data.get(riskteam.risk_team_id)  
            if team is None:
                team = {'team_name' : riskteam.description, 'levels': copy.deepcopy(d), 'id': riskteam.risk_team_id}
            team['index'] = index
            index+=1
            data[riskteam.risk_team_id] =  team
            #print data[row[0]]['levels']
            #data[row[0]]['levels'].sort()
        return data, program
        
    
from sqlalchemy.ext.declarative import declarative_base 
Base = declarative_base() 
class MyTest (Base):
    __tablename__ = 'my_test';
    __table_args__  = ( saschema.UniqueConstraint("entitytype","key"), {} ) 
    id         = saschema.Column(Integer, primary_key=True)
    key        = saschema.Column(Unicode(16))
    entitytype = saschema.Column(String(32)) 

class RiskResponsible(DeclarativeBase):
    __tablename__ = 'risk_responsible';
    
    risk_responsible_id = Column(Integer, autoincrement=True, primary_key=True);
    detail = Column(   Text, nullable=False);
    
    risk_management_id = Column(   Integer,ForeignKey('risk_management.risk_management_id'), nullable=False, index=True) ;
    risk_management = relation('RiskManagement', backref='riskresponsible');
    
    risk_team_id = Column(   Integer,ForeignKey('risk_team.risk_team_id'), nullable=False, index=True) ;
    risk_team = relation('RiskTeam', backref='riskresponsible');
    
    report_date =  Column(DateTime, nullable=False, default=datetime.now);
    create_date =  Column(DateTime, nullable=False, default=datetime.now);
     
    def __init__(self):
        self.risk_responsible_id = None;
        self.detail = None;
        self.risk_management_id = 0;
        self.risk_team_id = 0;
    
        self.report_date =  datetime.now();
        self.create_date =  datetime.now();
    
        
    def save(self):
        DBSession.add(self); 
        DBSession.flush() ;
    
    def update(self):
        DBSession.update(self);
        
    def remove(self):
        DBSession.delete(self);
        DBSession.flush() ;   
    
    @classmethod
    def getById(cls,id):
        return DBSession.query(cls) .get(id); 
        
    @classmethod
    def saveByTeam(cls,teams=None,risk_management = None):
        log.info("saveByTeam");
        if(teams is not None and risk_management is not None):
            listteam = teams.split(',');
            """  oldresponse =[];
            oldHash = {};
            if(len(listteam) >0):
                oldresponse = RiskResponsible.listByRiskManage(risk_management);
                log.info("len " + str(len(oldresponse)));
                for o in oldresponse:
                    oldHash[o.risk_team_id] = o;
            """
            
                     
            for team in listteam:
                response = RiskResponsible.getTeamByTeamTypeAndRiskManage(team,risk_management);
                 
                #insert 
                if(len(response) == 0):
                    riskresponse = RiskResponsible();
                    riskresponse.risk_management_id = risk_management;
                    riskresponse.risk_team_id = team;
                    riskresponse.create_date =  datetime.now();
                    riskresponse.detail = "";
                    riskresponse.save();
                
                    
        pass;
    
    @classmethod
    def removeRiskManage(cls,risk_management=None):
        sql = "delete from risk_responsible where risk_management_id =" +str(risk_management) ;
        #sql = "update risk_responsible set active = '0' where risk_management_id =" +str(risk_management) ;
        result = DBSession.execute(sql);
    @classmethod
    def removeExclusiveOf(cls,remove_Respon=None,risk_management=None):
        #DBSession.delete(cls).filter(  and_( not_(cls.risk_team_id.in_(listteam)), cls.risk_management_id == str(risk_management) )   )
        sql = "delete from risk_responsible where risk_management_id =" +str(risk_management)+ " and risk_team_id not in ("+ str(remove_Respon) + ") ";
        #sql = "update risk_responsible set active = '0' where risk_management_id =" +str(risk_management)+ " and risk_team_id not in ("+ str(remove_Respon) + ") "
        result = DBSession.execute(sql);
    @classmethod
    def listByRiskManage(cls,risk_management=None):
        return DBSession.query(cls).filter(  cls.risk_management_id == str(risk_management)  ).order_by(cls.risk_team_id).all();
    
    @classmethod
    def listByTeamsAndRiskManage(cls,listteam=None,risk_management=None):
        
        return DBSession.query(cls).filter(  and_(cls.risk_team_id.in_(listteam), cls.risk_management_id == str(risk_management) )   ).order_by(cls.risk_team_id).all();
    @classmethod
    def getTeamByTeamTypeAndRiskManage(cls,risk_team=None, risk_management=None):
        return DBSession.query(cls).filter(  and_(cls.risk_team_id == str(risk_team), cls.risk_management_id == str(risk_management) )   ).order_by(cls.risk_team_id).all();
    
    @classmethod
    def getSectionTeam(cls,team_type=None,risk_management=None,risk_section=None):
        list = [];
        if( team_type is not None and risk_management is not None and risk_section is not None):
            sql = "risk_team.risk_team_type_id ='"+str(team_type)+"' and risk_responsible.risk_management_id = "+str(risk_management) +" and  section_list_team.risk_section_id = "+ str(risk_section); 
            
            sql = text("""  select risk_responsible.risk_team_id
                         FROM    
                            risk_responsible
                            INNER JOIN risk_team on risk_responsible.risk_team_id = risk_team.risk_team_id
                            LEFT OUTER JOIN section_list_team on risk_team.risk_team_id = section_list_team.risk_team_id
                            LEFT OUTER JOIN risk_section on risk_section.risk_section_id = section_list_team.risk_section_id
                        WHERE """ + sql);
            result = DBSession.execute(sql);
    
        
            for row in result:
                list.append(row['risk_team_id']);
           
        
        return list;            
                            
                            
        return list;    
    
    @classmethod
    def getResultTeamByRiskId(cls,risk_id=None):
        list = [];
        if(risk_id ):
            sql = text (
                        """
                        select 
                            risk_team.description as risk_team,
                            risk_responsible.detail as result
                        from 
                            risk_responsible LEFT OUTER JOIN  risk_team on risk_team.risk_team_id = risk_responsible.risk_team_id
                        where 
                            risk_responsible.risk_management_id = """ + str( risk_id) + """
                        """
                        );
            result = DBSession.execute(sql);
            
            for row in result:
                list.append({  'risk_team':row['risk_team'],    'result':row['result']  });
        
        return list;
    @classmethod
    def getSectionTeamArray(cls ,team_type=None, risk_management=None):
        list = [];
        if(team_type is not None and risk_management is not None):
            
            
            sql = "risk_team.risk_team_type_id ="+str(team_type)+" and  risk_responsible.risk_management_id = "+str(risk_management);
        
            sql = text("""select risk_responsible.risk_team_id
                from risk_responsible INNER JOIN risk_team on risk_responsible.risk_team_id = risk_team.risk_team_id
                WHERE """+sql);
        
        
            result = DBSession.execute(sql);
    
        
            for row in result:
                list.append(row['risk_team_id']);
           
        
        return list;
    
    @classmethod
    def updateDetailByTeamAndRisk(cls,team=None,risk_management =None,detail=None):
        
        if(team and risk_management):
            responsed = DBSession.query(cls).filter(  and_(cls.risk_team_id == str(team), cls.risk_management_id == str(risk_management) )   ).order_by(cls.risk_team_id).first();
            responsed.detail = str(detail);
         
        pass;
    
    def getResp(self,report_date):
        
        #reportdate = resp.report_date.replace(year = resp.report_date.year + 543)
        self.total_date = (self.report_date  - report_date ).days
        if self.total_date ==0:
            self.total_date = 1
        #print "total %s " %total_date.days
        #value.append({'service_name': resp.risk_team.description, 'detail' : resp.detail,'report_date':  reportdate.strftime('%d/%m/%Y %H:%M') if len(resp.detail) >0 else ''   })
        return {'service_name': self.risk_team.description, 'detail' : self.detail,'report_date':   str(self.total_date).decode('UTF8') + str(' วัน').decode('UTF8')    if len(self.detail) > 0 else ''   }
    
    

class UserRiskSection(DeclarativeBase):
    __tablename__ = 'user_risk_section';
    
    user_risk_section_id = Column(Integer, autoincrement=True, primary_key=True);
    user_id = Column(   Integer,ForeignKey('tg_user.user_id'), nullable=False, index=True) ;
    risk_section_id = Column(   Integer,ForeignKey('risk_section.risk_section_id'), nullable=False, index=True) ;
    
    def __init__(self):
        self.user_risk_section_id = None;
        self.user_id = 0;
        self.risk_section_id = 0;
    
    @classmethod
    def getByUserName(cls,username=None):
        
        a = DBSession.query(User, cls).filter(User.user_id==cls.user_id).filter(User.user_name==username).first();
        if(a):
            return a[1]; 
        else:
            return None;
            
        
    @classmethod
    def getByUserId(cls,userid=None):
        return DBSession.query(cls).filter(  cls.user_id == str(userid) ).first();
    
    @classmethod
    def getSectionByUser(cls,username):
        sql = text("""
                        select 
                            user_risk_section.risk_section_id
                        from 
                            tg_user INNER JOIN user_risk_section on tg_user.user_id = user_risk_section.user_id
                        WHERE
                            tg_user.user_name = '""" + username +"""'   """);
        result = DBSession.execute(sql);
        risk_section_id = "";
        for row in result:
                risk_section_id =  row['risk_section_id'] ;
        return risk_section_id ;
    
class SectionListTeam(DeclarativeBase):
    __tablename__ = 'section_list_team';
    
    section_list_team_id = Column(Integer, autoincrement=True, primary_key=True);
    risk_section_id = Column(   Integer,ForeignKey('risk_section.risk_section_id'), nullable=False, index=True) ;
    risk_team_id = Column(   Integer,ForeignKey('risk_team.risk_team_id'), nullable=False, index=True) ;
    
    def __init__(self):
        self.section_list_team_id = None;
        self.risk_section_id = 0;
        self.risk_team_id = 0;
        
    @classmethod
    def getSectionBySectionId(cls,sectionid):
        return DBSession.query(cls).filter(  cls.risk_section_id == str(sectionid) ).first();
    
     
    
class Questionnaires(DeclarativeBase):
    __tablename__ = 'questionnaires';
    
    id = Column(Integer, autoincrement=True, primary_key=True);
    sex = Column(Integer, nullable=False, index=True );
    section = Column(String(255) , nullable=False);
    ao1 = Column(Integer, nullable=False); 
    an1 = Column(Integer, nullable=False);
     
    ao2 = Column(Integer, nullable=False);  
    an2 = Column(Integer, nullable=False);     
     
    ao3 = Column(Integer, nullable=False);  
    an3 = Column(Integer, nullable=False); 
     
    ao4 = Column(Integer, nullable=False);  
    an4 = Column(Integer, nullable=False); 
     
    ao5 = Column(Integer, nullable=False);  
    an5 = Column(Integer, nullable=False); 
     
    ao6 = Column(Integer, nullable=False);  
    an6 = Column(Integer, nullable=False);
    
         
    bo1 = Column(Integer, nullable=False);
    bn1 = Column(Integer, nullable=False); 
    
    bo2 = Column(Integer, nullable=False);
    bn2 = Column(Integer, nullable=False);
    
    bo3 = Column(Integer, nullable=False);
    bn3 = Column(Integer, nullable=False);
    
    bo4 = Column(Integer, nullable=False);
    bn4 = Column(Integer, nullable=False);
    
    bo5 = Column(Integer, nullable=False);
    bn5 = Column(Integer, nullable=False);
    
    bo6 = Column(Integer, nullable=False);
    bn6 = Column(Integer, nullable=False);
    
    bo7 = Column(Integer, nullable=False);
    bn7 = Column(Integer, nullable=False);
    
    
    co1 = Column(Integer, nullable=False);
    cn1 = Column(Integer, nullable=False);
    
    co2 = Column(Integer, nullable=False);
    cn2 = Column(Integer, nullable=False);    
    
    co3 = Column(Integer, nullable=False);
    cn3 = Column(Integer, nullable=False);
    
    @classmethod
    def queryBySumLevelBy(cls,column1=None,column2=None):
        sql1 = None;
        sql2 = None;
        sql = "select  ";
        if column1 :
            sql1 = "";
            sql1 = sql1 + " sum(IF("+ str(column1) + " = 1,1,0)) as " + str(column1) + "_1 ,"; 
            sql1 = sql1 + " sum(IF("+ str(column1) + " = 2,1,0)) as " + str(column1) + "_2 ,";
            sql1 = sql1 + " sum(IF("+ str(column1) + " = 3,1,0)) as " + str(column1) + "_3 ,";
            sql1 = sql1 + " sum(IF("+ str(column1) + " = 4,1,0)) as " + str(column1) + "_4 ,";
            sql1 = sql1 + " sum(IF("+ str(column1) + " = 5,1,0)) as " + str(column1) + "_5 ,";
            
            sql1 = sql1 + " (sum(IF("+ str(column1) + " = 1,1,0))/count(*))*100 as " + str(column1) + "_p1 ,";
            sql1 = sql1 + " (sum(IF("+ str(column1) + " = 2,1,0))/count(*))*100 as " + str(column1) + "_p2 ,";
            sql1 = sql1 + " (sum(IF("+ str(column1) + " = 3,1,0))/count(*))*100 as " + str(column1) + "_p3 ,";
            sql1 = sql1 + " (sum(IF("+ str(column1) + " = 4,1,0))/count(*))*100 as " + str(column1) + "_p4 ,";
            sql1 = sql1 + " (sum(IF("+ str(column1) + " = 5,1,0))/count(*))*100 as " + str(column1) + "_p5 ";
            
        if column2 :
            sql2 = "";
            sql2 = sql2 + " sum(IF("+ str(column2) + " = 1,1,0)) as " + str(column2) + "_1 ,"; 
            sql2 = sql2 + " sum(IF("+ str(column2) + " = 2,1,0)) as " + str(column2) + "_2 ,";
            sql2 = sql2 + " sum(IF("+ str(column2) + " = 3,1,0)) as " + str(column2) + "_3 ,";
            sql2 = sql2 + " sum(IF("+ str(column2) + " = 4,1,0)) as " + str(column2) + "_4 ,";
            sql2 = sql2 + " sum(IF("+ str(column2) + " = 5,1,0)) as " + str(column2) + "_5, ";
            
            sql2 = sql2 + " (sum(IF("+ str(column2) + " = 1,1,0))/count(*))*100 as " + str(column2) + "_p1 ,";
            sql2 = sql2 + " (sum(IF("+ str(column2) + " = 2,1,0))/count(*))*100 as " + str(column2) + "_p2 ,";
            sql2 = sql2 + " (sum(IF("+ str(column2) + " = 3,1,0))/count(*))*100 as " + str(column2) + "_p3 ,";
            sql2 = sql2 + " (sum(IF("+ str(column2) + " = 4,1,0))/count(*))*100 as " + str(column2) + "_p4 ,";
            sql2 = sql2 + " (sum(IF("+ str(column2) + " = 5,1,0))/count(*))*100 as " + str(column2) + "_p5 ";
            
        if sql1 and sql2 :
            sql = sql + sql1 + " , " + sql2;
        elif sql1:
            sql = sql + sql1;
        elif sql2:
            sql = sql + sql2;
        else :
            sql = sql + "*";
                   
        sql = sql + " from questionnaires" ;
        
        result = DBSession.execute(sql);
        list =[];
        for row in result:
            if column1 and column2:
                list.append({ 'name':'1'
                            , 'old':row[column1+"_1"]
                            , 'new':row[column2+"_1"] 
                            
                            , 'pold':row[column1+"_p1"]
                            , 'pnew':row[column2+"_p1"]                               
                            });
                
                list.append({ 'name':'2'
                            , 'old':row[column1+"_2"]
                            , 'new':row[column2+"_2"]    
                            
                            , 'pold':row[column1+"_p2"]
                            , 'pnew':row[column2+"_p2"]                               
                            });
                            
                list.append({ 'name':'3'
                            , 'old':row[column1+"_3"]
                            , 'new':row[column2+"_3"]     
                            
                            , 'pold':row[column1+"_p3"]
                            , 'pnew':row[column2+"_p3"]                              
                            });
                
                list.append({ 'name':'4'
                            , 'old':row[column1+"_4"]
                            , 'new':row[column2+"_4"]
                            
                            , 'pold':row[column1+"_p4"]
                            , 'pnew':row[column2+"_p4"]                                   
                            });
                
                list.append({ 'name':'5'
                            , 'old':row[column1+"_5"]
                            , 'new':row[column2+"_5"]
                            
                            , 'pold':row[column1+"_p5"]
                            , 'pnew':row[column2+"_p5"]                                   
                            });
                            
            elif column1:
                list.append({ 'name':'1'
                            , 'old':row[column1+"_1"]
                            
                            , 'pold':row[column1+"_p1"] 
                                                          
                            });
                
                list.append({ 'name':'2'
                            , 'old':row[column1+"_2"]   
                            
                            , 'pold':row[column1+"_p2"]                          
                            });
                            
                list.append({ 'name':'3'
                            , 'old':row[column1+"_3"] 
                            
                            
                            , 'pold':row[column1+"_p3"]                              
                            });
                
                list.append({ 'name':'4'
                            , 'old':row[column1+"_4"]
                            , 'pold':row[column1+"_p4"]                             
                            });
                
                list.append({ 'name':'5'
                            , 'old':row[column1+"_5"]
                            
                            , 'pold':row[column1+"_p5"]                               
                            });
            elif column2:
                list.append({ 'name':'1'
                            , 'new':row[column2+"_1"]
                            
                            , 'pnew':row[column2+"_p1"]                                
                            });
                
                list.append({ 'name':'2'
                            , 'new':row[column2+"_2"]   
                             , 'pnew':row[column2+"_p2"]                             
                            });
                            
                list.append({ 'name':'3'
                            , 'new':row[column2+"_3"] 
                             , 'pnew':row[column2+"_p3"]                               
                            });
                
                list.append({ 'name':'4'
                            , 'new':row[column2+"_4"] 
                             , 'pnew':row[column2+"_p4"]                               
                            });
                
                list.append({ 'name':'5' 
                            , 'new':row[column2+"_5"] 
                             , 'pnew':row[column2+"_p5"]                               
                            });
        return list;
    
    @classmethod
    def queryByMedianGroup(cls,group=None):
        list =[];
        row = 0;
        if group:
            if (group == 1):
                sql = text("""select "เวลาในการจัดทำสรุปรายงาน" as name, avg(ao1) as m_o, STD(ao1) as std_o, avg( an1)  as m_n, STD(an1) as std_n from questionnaires
                                UNION
                                select  "เวลาในการจัดแยกรายงานเพื่อนำส่งและตอบกลับของหน่วยงาน" as name, avg(ao2)  as m_o, STD(ao2) as std_o, avg( an2)  as m_n, STD(an2) as std_n from questionnaires
                                UNION
                                select  "เวลาในการรวบรวมเอกสาร" as name, avg(ao3)  as m_o, STD(ao3) as std_o, avg( an3) as m_n, STD(an3) as std_n from questionnaires
                                UNION
                                select  "เวลาในการแปรผลข้อมูล" as name, avg(ao4) as m_o, STD(ao4) as std_o, avg( an4) as m_n, STD(an4) as std_n from questionnaires
                                UNION
                                select  "ลดขั้นตอนการทำงาน" as name, avg(ao5)  as m_o, STD(ao5) as std_o, avg( an5)  as m_n, STD(an5) as std_n from questionnaires
                                UNION
                                select "ประมวลผลรวดเร็ว ถูกต้อง แม่นยำ" as name,  avg(ao6)  as m_o, STD(ao6) as std_o, avg( an6)  as m_n, STD(an6) as std_n from questionnaires""");
                result = DBSession.execute(sql);
                row = row +1;
                for row in result:
                    list.append(
                                 {'id': row,'m_old': row['m_o'], 'm_new':row['m_n'],
                                  'std_old': row['std_o'],'std_new': row['std_n'],
                                  'name': row['name']}
                                 );
                                
        return list;
    
    @classmethod
    def queryByAvgBy(cls,column1=None,column2=None):
        sql1 = None;
        sql2 = None;
        sql = "select  ";
        if column1 :
            sql1 = "";
             
            sql1 = sql1 + " AVG("+ str(column1) + ") as m_" + str(column1)  ; 
           
        if column2 :
            sql2 = "";
             
            sql2 = sql2 + " AVG("+ str(column2) + ") as m_" + str(column2)  ; 
            
        
        if sql1 and sql2 :
            sql = sql + sql1 + " , " + sql2;
        elif sql1:
            sql = sql + sql1;
        elif sql2:
            sql = sql + sql2;
        else :
            sql = sql + "*";
                   
        sql = sql + " from questionnaires" ;
        
        result = DBSession.execute(sql);
        list =[];
        for row in result:
            if column1 and column2:
                list.append({ 'name': ' '  #column1 + column2
                            , 'm_old':row["m_" + column1 ]
                            , 'm_new':row["m_" + column2 ] 
                                                            
                            });
            elif column1:
                list.append({ 'name':column1 
                            , 'm_old':row["m_" + column1 ] 
                                                            
                            });
            elif column2:
                list.append({ 'name': column2                           
                            , 'm_new':row["m_" + column2 ] 
                                                            
                            });
             
        return list;         
                
