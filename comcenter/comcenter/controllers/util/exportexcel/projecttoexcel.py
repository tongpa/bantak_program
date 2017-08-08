# coding=utf8
from tempfile import TemporaryFile,gettempdir;
import os as _os;
from xlwt import Workbook,XFStyle;
from datetime import datetime,date,time,timedelta;
import calendar;
 
class ProjectToExcel(object):
    
    def __init__(self):
        pass;
    
    def exportToExcel(self,objectProject):
        
        book = Workbook();
        sheet1 = book.add_sheet('Sheet 1')
        if( objectProject):
            i=0;
            
            row1 = sheet1.row(i) ;
            row1.write(0, ('ประเภท').decode('UTF8') );
            row1.write(1, ('ชื่อโครงการ').decode('UTF8'));
            
            row1.write(2, ('รายละเอืยด').decode('UTF8') );
            row1.write(3, ('งบประมาณรวม').decode('UTF8') );
            row1.write(4, ('งบประมาณ').decode('UTF8') );
            row1.write(5, ('เงินบำรุง').decode('UTF8') );
            row1.write(6, ('งบประมาณอื่น').decode('UTF8') );
            row1.write(7, ('งบประมาณอื่นจาก').decode('UTF8') );
            row1.write(8, ('ผู้รับผิดชอบ').decode('UTF8') );
            row1.write(9, ('กลุ่ม').decode('UTF8') );
            row1.write(10, ('หน่วย/งาน').decode('UTF8') );
            
            i=i+1; 
            style = XFStyle();
            style.num_format_str = '#,##0.00';
            
            for value in  objectProject:
                
                row1 = sheet1.row(i) ;
                
                row1.write(0, value.get('project_type').decode('UTF8') );
                row1.write(1, value.get('project_name').decode('UTF8') );
                 
                row1.write(2, value.get('detail').decode('UTF8') );
                row1.write(3, value.get('allBudget') ,style  );
                row1.write(4, value.get('project_budget'  ) ,style  );
                row1.write(5, value.get('maintenance_funds_budget'),style   );
                row1.write(6, value.get('budget_other') ,style  );
               
                if(value.get('budget_other_from')):
                    row1.write(7, value.get('budget_other_from').decode('UTF8') );
                if(value.get('user_name')):
                    row1.write(8, value.get('user_name').decode('UTF8') );
                
                row1.write(9, value.get('division').decode('UTF8') );
                row1.write(10, value.get('section').decode('UTF8') );
                 
                 
                i=i+1; 
        
         
        dirTempFile = gettempdir() + _os.sep + str('simple.xls');
                
        book.save(dirTempFile);
        #book.save(TemporaryFile());
        
        return dirTempFile;
         
        
        
         