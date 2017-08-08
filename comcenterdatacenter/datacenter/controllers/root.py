# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController
from tg import expose, flash, require, url, lurl, request, redirect, validate, session, response
from tg.i18n import set_lang,get_lang, ugettext as _
from tgext.pluggable import app_model

from comcenter.controllers.util.utility import Utility
#from comcenter.controllers.util.exportexcel.projecttoexcel import ProjectToExcel;
from datetime import datetime,date,time,timedelta;
from json import loads;


import logging;
import sys;
log = logging.getLogger(__name__);

class RootController(TGController):
    
    def __init__(self):
        self.util = Utility();

        
    @expose('datacenter.templates.datacenters.index')
    def index(self):
        print "Index maintenance";
        """Handle the front-page."""
        set_lang("th"); 
        session['lang'] = "th";
        session.save();
        userid = "";
        
            #print "user : " + str(userid);
        return dict(page='datacenter')
    
    @expose('json')
    def getMenu(self,**kw):
        
        childrens =  [];
        
        children = [];
        
        #########1###############
        children.append({
                'text':'แสดงพื้นที่ อำเภอบ้านตาก ตำบล หมู่บ้าน',
                'id':'1',
                'leaf':True
            });
        children.append({
                'text':'เครือข่ายพัฒนาคุณภาพ',
                'id':'2',
                'leaf':True
            });
        children.append({
                'text':'พื้นที่รับผิดชอบของหน่วยบริการ',
                'id':'3',
                'leaf':True
            });
        
        childrens.append({
            'text':'1. แผนที่จังหวัดตาก',
            'children': children
        });    
        #2########################
        children = [];
        
        
        children.append({
                'text':'ข้อมูลอำเภอบ้านตาก ตำบล หมู่บ้าน',
                'id':'4',
                'leaf':True
            });
        children.append({
                'text':'หน่วยบริการสาธารณสุข',
                'id':'5',
                'leaf':True
            });
         
        children.append({
                'text':'สรุปทรัพยากรสาธารณสุข (DHS)',
                'id':'7',
                'leaf':True
            });
        childrens.append({
            'text':'2. ข้อมูลพื้นฐานทั่วไป',
            'children': children
        });  
        #3########################
        children = [];
        
        
        children.append({
                'text':'ทำเนียบผู้บริหารหน่วยงาน',
                'id':'8',
                'leaf':True
            });
        children.append({
                'text':'บุคลากรตามรายงาน/ตำแหน่ง',
                'id':'9',
                'leaf':True
            });
        children.append({
                'text':'บุคลากรตามประเภท(ข้ารายการ,ลูกจ้าง, พกส)',
                'id':'10',
                'leaf':True
            });
       
        childrens.append({
            'text':'3. ข้อมูลบุคลากรสาธารณสุข',
            'children': children
        });  
        
        #4########################
        children = [];
        
        
        children.append({
                'text':'ประชากรรายอำเภอ ตำบล หมู่บ้าน',
                'id':'11',
                'leaf':True
        });
        children.append({
                'text':'ประชากร รายหน่วยงาน',
                'id':'12',
                'leaf':True
        });
        children.append({
                'text':'โครงสร้างประชากร',
                'id':'13',
                'leaf':True
        });
        children.append({
                'text':'ประชากรแยกตามกลุ่มอายุ',
                'id':'14',
                'leaf':True
        });
        children.append({
                'text':'ประชากรรายอำเภอ ตำบล หมู่บ้าน',
                'id':'151',
                'leaf':True
        });
        children.append({
                'text':'ประชากรแยกรายอายุ และเพศ',
                'id':'161',
                'leaf':True
        });
        children.append({
                'text':'ประชากรกลุ่มเป้าหมายที่สำคัญ',
                'id':'171',
                'leaf':True
        });
        childrens.append({
            'text':'4. ข้อมูลประชากรปี 2557',
            'children': children
        });  
        
        #5########################
        children = [];
        
        
        children.append({
                'text':'อัตราเกิด อัตราตาย และอัตราเพิ่ม',
                'id':'16',
                'leaf':True
        });
        
        children.append({
                'text':'สาเหตุการตาย เปรียบเทียบรายปี',
                'id':'17',
                'leaf':True
        });
        children.append({
                'text':'สาเหตุการตายปี 2557',
                'id':'18',
                'leaf':True
        });
        children.append({
                'text':'ข้อมูลเด็กเกิด ปี 2557',
                'id':'19',
                'leaf':True
        });
        childrens.append({
            'text':'5. สถิติชีพพยาบาล',
            'children': children
        });  
        
        #6########################
        children = [];
        
        
        children.append({
                'text':'ผลการดำเนินงานตาม KPI ',
                'id':'20',
                'leaf':True
        });
        
        children.append({
                'text':'ผลการดำเนินงานตามตัวชี้วัดรวม ',
                'id':'21',
                'leaf':True
        });
        children.append({
                'text':'บันทึกผลงาน KPI ประจำเดือน',
                'id':'22',
                'leaf':True
        });
        childrens.append({
            'text':'6. การดำเนินงานตามตัวชี้วัด ปี 2557',
            'children': children
        });  
        
        #7########################
        children = [];
        
        
        children.append({
                'text':'สรุปความก้าวหน้าการเบิกจ่าย',
                'id':'23',
                'leaf':True
        });
        children.append({
                'text':'บันทึกแผนงาน และโครงการ',
                'id':'24',
                'leaf':True
        });
        
        childrens.append({
            'text':'7. แผนงานโครงการ ปี 2557',
            'children': children
        });  
        
        #8########################
        children = [];
        
        
        children.append({
                'text':'บันทึกรายรับ-รายจ่ายประจำเดือน',
                'id':'25',
                'leaf':True
        });
        
        children.append({
                'text':'ตรวจสอบข้อมูลเบื่องต้น',
                'id':'26',
                'leaf':True
        });
        
        children.append({
                'text':'สรุปผลเบิกจ่ายตามแผนการเงิน',
                'id':'27',
                'leaf':True
        });
        
        
        children.append({
                'text':'สถานะการเงิน การคลัง',
                'id':'28',
                'leaf':True
        });
        childrens.append({
            'text':'8. สถานการณ์ทางการเงิน',
            'children': children
        });  
        #9########################
        children = [];
        
        
        children.append({
                'text':'สัปดาห์ระบาดวิทยาปี 2557',
                'id':'29',
                'leaf':True
        });
        children.append({
                'text':'สถิติการส่งบัตร รายงาน 506',
                'id':'30',
                'leaf':True
        });
        children.append({
                'text':'ความทันเวลาส่งบัตรรายงาน',
                'id':'31',
                'leaf':True
        });
        children.append({
                'text':'อันดับโรคจากบัตรรายงาน 506',
                'id':'32',
                'leaf':True
        });
        children.append({
                'text':'สถานการณ์โรคจากรายงาน 506',
                'id':'33',
                'leaf':True
        });
        
        
        children.append({
                'text':'บันทึกบัตร รง506 สำหรับเอกชน และ ต่างจังหวัด',
                'id':'34',
                'leaf':True
        });
        childrens.append({
            'text':'9. ระบาดวิทยา 506 ปี 2557',
            'children': children
        });  
        
        #10########################
        children = [];
        
        
        children.append({
                'text':'สถานการณ์โรค รายโรค',
                'id':'35',
                'leaf':True
        });
        children.append({
                'text':'ไข้เลือดออก DHF',
                'id':'36',
                'leaf':True
        });
        
        children.append({
                'text':'โรคเอดส์',
                'id':'37',
                'leaf':True
        });
        
        children.append({
                'text':'โรคเบาหวาน ความดัน',
                'id':'38',
                'leaf':True
        });
        
        
        children.append({
                'text':'รายงาน สรุป NCD CD รายเดือน',
                'id':'39',
                'leaf':True
        });
        childrens.append({
            'text':'10. สถานการณ์โรค CD และ NCD',
            'children': children
        });  
        
        #11########################
        children = [];
        
        
        children.append({
                'text':'ผลการบำบัดรักษาและติดตาม',
                'id':'40',
                'leaf':True
        });
        children.append({
                'text':'Upload ปสต 3-5',
                'id':'41',
                'leaf':True
        });
        childrens.append({
            'text':'11. ผลการบำบัดรักษาเสพติด',
            'children': children
        });  
        
        #12########################
        children = [];
        
        
        children.append({
                'text':'สรุปผู้รับบริการ OP IP PP รายพื้นที่',
                'id':'42',
                'leaf':True
        });
        children.append({
                'text':'รายงาน 0110 รง5 ปี 2557',
                'id':'43',
                'leaf':True
        });
        childrens.append({
            'text':'12. รายงานการบริการด้านการรักาาพยาบาล',
            'children': children
        });  
         
        
        
        return dict(text= '.' ,children =  childrens);
        

