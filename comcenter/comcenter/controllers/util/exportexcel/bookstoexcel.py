# coding=utf8
from tempfile import TemporaryFile,gettempdir;
import os as _os;
from xlwt import Workbook,XFStyle;
from datetime import datetime,date,time,timedelta;
import calendar;
 
class BooksToExcel(object):
    
    def __init__(self):
        pass;
    
    def exportToExcel(self,objectBooks):
        
        book = Workbook();
        sheet1 = book.add_sheet('Sheet 1')
        if( objectBooks):
            i=0;
            
            row1 = sheet1.row(i) ;
            row1.write(0, ('เลขทะเบียน').decode('UTF8') );
            row1.write(1, ('ที่').decode('UTF8'));
            
            row1.write(2, ('ลงวันที่').decode('UTF8') );
            row1.write(3, ('จาก').decode('UTF8') );
            row1.write(4, ('ถึง').decode('UTF8') );
            row1.write(5, ('เรื่อง').decode('UTF8') );
            row1.write(6, ('การปฏิบัติ').decode('UTF8') );
            row1.write(7, ('หมายเหตุ').decode('UTF8') );
            
            
            i=i+1; 
            style = XFStyle();
            style.num_format_str = 'D-MMM-YY';
            
            for value in  objectBooks:
                
                row1 = sheet1.row(i) ;
                
                row1.write(0, value.get('book_number').decode('UTF8') );
                row1.write(1, value.get('book_at').decode('UTF8') );
                 
                row1.write(2, value.get('book_recive') ,style );
                row1.write(3, value.get('book_from').decode('UTF8')   );
                row1.write(4, value.get('book_to'  ).decode('UTF8')   );
                row1.write(5, value.get('book_detail').decode('UTF8')    );
                row1.write(6, value.get('book_operations').decode('UTF8')  );
                row1.write(7, value.get('book_remark').decode('UTF8') );
                #row1.write(7, value.get('book_type_name').decode('UTF8') );
                 
                 
                 
                i=i+1; 
        
         
        dirTempFile = gettempdir() + _os.sep + str('books.xls');
                
        book.save(dirTempFile);
        #book.save(TemporaryFile());
        
        return dirTempFile;
         
        
        
       