# coding=utf8
from tempfile import TemporaryFile,gettempdir;
import os as _os;
from xlwt import Workbook,XFStyle,Alignment, Font,Borders,Pattern;
from datetime import datetime,date,time,timedelta;
import calendar;

class RiskToExcel(object):
    
    def __init__(self):
        pass;
    
    def exportReport1ToExcel(self,objectProject):
        book = Workbook();
        sheet1 = book.add_sheet('Sheet 1');
        sheet1.col(1).width = 256*20;
        sheet1.col(2).width = 256*80;
        sheet1.col(3).width = 256*10;
        sheet1.col(4).width = 256*10;
        sheet1.col(5).width = 256*20;
        sheet1.col(6).width = 256*20;
        
        borders = Borders()
        borders.left = Borders.THIN
        borders.right = Borders.THIN
        borders.top = Borders.THIN
        borders.bottom = Borders.THIN
        
        pattern = Pattern();
        pattern.pattern = Pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = 23
    
        wrap = Alignment();
        wrap.wrap = 1;
        wrap.vert = Alignment.VERT_TOP
        
        alignHeader =  Alignment();
        alignHeader.horz = Alignment.HORZ_CENTER;
    
        alignTop =  Alignment();
        alignTop.vert = Alignment.VERT_TOP    
        
        fnt = Font()
        fnt.name = 'Arial'
        fnt.colour_index = 4
        fnt.bold = True
        
        styleWrap = XFStyle();
        styleWrap.alignment = wrap;
        
        styleHead = XFStyle();
        styleHead.font = fnt;
        styleHead.borders = borders;
        styleHead.pattern = pattern;
        styleHead.alignment = alignHeader;
        
        styleRowDetail = XFStyle();
        styleRowDetail.borders = borders;
        styleRowDetail.alignment = alignTop;
        
        styleDate = XFStyle()
        styleDate.num_format_str = 'DD-MM-YYYY'   ;   #'D-MMM-YY';
        styleDate.borders = borders;
        styleDate.alignment = alignTop;
        
        StyleRowDetailWrap = styleRowDetail ;
        StyleRowDetailWrap.alignment = wrap;
        
        
        if( objectProject):
            i=0;
            
            row1 = sheet1.row(i) ;
            row1.write(0, ('ลำดับที่').decode('UTF8') ,styleHead);
            #sheet1.write_merge(i, i, 1, 2,  ('รายละเอียด').decode('UTF8')    );
            row1.write(1, ('เลขความเสี่ยง').decode('UTF8'),styleHead );
            row1.write(2, ('อุบัติการณ์/ภาวะไม่พึงประสงค์').decode('UTF8'),styleHead);  
            
            row1.write(3, ('วันที่รายงาน').decode('UTF8'),styleHead );
            row1.write(4, ('ความรุนแรง').decode('UTF8'),styleHead );
            row1.write(5, ('ด้าน/โปรแกรม').decode('UTF8') ,styleHead);
            row1.write(6, ('หน่วยที่รายงาน').decode('UTF8') ,styleHead);
            
            i=i+1;
             
            for value in  objectProject:
                row1 = sheet1.row(i) ;
                row1.write(0, value.get('row')  ,styleRowDetail );
                row1.write(1, str(value.get('risk_id')).decode('UTF8'),styleRowDetail );
                row1.write(2, value.get('detail').decode('UTF8'),StyleRowDetailWrap );
                row1.write(3, value.get('report_date') ,styleDate );
                row1.write(4, value.get('level').decode('UTF8')  ,styleRowDetail   );
                row1.write(5, value.get('pro').decode('UTF8')  ,styleRowDetail   );                
                row1.write(6, value.get('reporter').decode('UTF8')  ,styleRowDetail   );
                i=i+1;
                
                row2 = sheet1.row(i) ;
                row2.write(2, ('รายละเอียด').decode('UTF8'),styleHead);       
                row2.write(3, ('หน่วยที่ตอบ').decode('UTF8'),styleHead );
                row2.write(4, ('ระยะเวลาตอบ').decode('UTF8'),styleHead );
                i=i+1;
                for resp in value.get('responsible'):
                    row2 = sheet1.row(i) ;
                    row2.write(2, str(resp.get('detail')).decode('UTF8'),StyleRowDetailWrap);       
                    row2.write(3, str(resp.get('service_name')).decode('UTF8'),styleRowDetail );
                    row2.write(4, str(resp.get('report_date')).decode('UTF8'),styleRowDetail );
                    i=i+1;
                    
        dirTempFile = gettempdir() + _os.sep + str('simpleReport1.xls');        
        book.save(dirTempFile);          
        return dirTempFile;
    
    def exportReport1ToExcel_old(self,objectProject):
        book = Workbook();
        sheet1 = book.add_sheet('Sheet 1');
        sheet1.col(1).width = 256*80;
        sheet1.col(2).width = 256*10;
        sheet1.col(3).width = 256*10;
        sheet1.col(4).width = 256*20;
        sheet1.col(5).width = 256*20;
        borders = Borders()
        borders.left = Borders.THIN
        borders.right = Borders.THIN
        borders.top = Borders.THIN
        borders.bottom = Borders.THIN
        
        pattern = Pattern();
        pattern.pattern = Pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = 23
    
        wrap = Alignment();
        wrap.wrap = 1;
        wrap.vert = Alignment.VERT_TOP
        
        alignHeader =  Alignment();
        alignHeader.horz = Alignment.HORZ_CENTER;
    
        alignTop =  Alignment();
        alignTop.vert = Alignment.VERT_TOP    
        
        fnt = Font()
        fnt.name = 'Arial'
        fnt.colour_index = 4
        fnt.bold = True
        
        styleWrap = XFStyle();
        styleWrap.alignment = wrap;
        
        styleHead = XFStyle();
        styleHead.font = fnt;
        styleHead.borders = borders;
        styleHead.pattern = pattern;
        styleHead.alignment = alignHeader;
        
        styleRowDetail = XFStyle();
        styleRowDetail.borders = borders;
        styleRowDetail.alignment = alignTop;
        
        styleDate = XFStyle()
        styleDate.num_format_str = 'DD-MM-YYYY'   ;   #'D-MMM-YY';
        styleDate.borders = borders;
        styleDate.alignment = alignTop;
        
        StyleRowDetailWrap = styleRowDetail ;
        StyleRowDetailWrap.alignment = wrap;
        
        
        if( objectProject):
            i=0;
            
            row1 = sheet1.row(i) ;
            row1.write(0, ('ลำดับที่').decode('UTF8') ,styleHead);
            #sheet1.write_merge(i, i, 1, 2,  ('รายละเอียด').decode('UTF8')    );
            
            row1.write(1, ('อุบัติการณ์/ภาวะไม่พึงประสงค์').decode('UTF8'),styleHead);       
            row1.write(2, ('วันที่รายงาน').decode('UTF8'),styleHead );
            row1.write(3, ('ความรุนแรง').decode('UTF8'),styleHead );
            row1.write(4, ('ด้าน/โปรแกรม').decode('UTF8') ,styleHead);
            row1.write(5, ('หน่วยที่รายงาน').decode('UTF8') ,styleHead);
            
            i=i+1;
             
            for value in  objectProject:
                row1 = sheet1.row(i) ;
                row1.write(0, value.get('row')  ,styleRowDetail );
                row1.write(1, value.get('detail').decode('UTF8'),StyleRowDetailWrap );
                row1.write(2, value.get('report_date') ,styleDate );
                row1.write(3, value.get('level').decode('UTF8')  ,styleRowDetail   );
                row1.write(4, value.get('pro').decode('UTF8')  ,styleRowDetail   );                
                row1.write(5, value.get('reporter').decode('UTF8')  ,styleRowDetail   );
                i=i+1;
        
        dirTempFile = gettempdir() + _os.sep + str('simpleReport1.xls');        
        book.save(dirTempFile);          
        return dirTempFile;

    def exportReport5ToExcel(self,objectProject):
        book = Workbook();
        sheet1 = book.add_sheet('Sheet 1');
        sheet1.col(1).width = 256*80;
        sheet1.col(2).width = 256*10;
        sheet1.col(3).width = 256*20;
        
        borders = Borders()
        borders.left = Borders.THIN
        borders.right = Borders.THIN
        borders.top = Borders.THIN
        borders.bottom = Borders.THIN
        
        pattern = Pattern();
        pattern.pattern = Pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = 23
    
        wrap = Alignment();
        wrap.wrap = 1;
        wrap.vert = Alignment.VERT_TOP
        
        alignHeader =  Alignment();
        alignHeader.horz = Alignment.HORZ_CENTER;
    
        alignTop =  Alignment();
        alignTop.vert = Alignment.VERT_TOP    
        
        fnt = Font()
        fnt.name = 'Arial'
        fnt.colour_index = 4
        fnt.bold = True
        
        styleWrap = XFStyle();
        styleWrap.alignment = wrap;
        
        styleHead = XFStyle();
        styleHead.font = fnt;
        styleHead.borders = borders;
        styleHead.pattern = pattern;
        styleHead.alignment = alignHeader;
        
        styleRowDetail = XFStyle();
        styleRowDetail.borders = borders;
        styleRowDetail.alignment = alignTop;
        
        styleDate = XFStyle()
        styleDate.num_format_str = 'DD-MM-YYYY'   ;   #'D-MMM-YY';
        styleDate.borders = borders;
        styleDate.alignment = alignTop;
        
        StyleRowDetailWrap = styleRowDetail ;
        StyleRowDetailWrap.alignment = wrap;
                
        if( objectProject):
            i=0;
            
            
            
            row1 = sheet1.row(i) ;
            row1.write(0, ('risk id').decode('UTF8'),styleHead );
            #sheet1.write_merge(i, i, 1, 2,  ('รายละเอียด').decode('UTF8')    );
            
            row1.write(1, ('รายละเอียด').decode('UTF8'),styleHead);
            
            row1.write(2, ('วันที่รายงาน').decode('UTF8'),styleHead );
            row1.write(3, ('หน่วยที่รายงาน').decode('UTF8') ,styleHead);
            
            
           
            
            i=i+1;
             
            for value in  objectProject:
                row1 = sheet1.row(i) ;
                row1.write(0, value.get('risk_management_id') ,styleRowDetail );
                row1.write(1, value.get('risk_detail').decode('UTF8'),StyleRowDetailWrap );
                #sheet1.write_merge(i, i, 1, 2,   value.get('risk_detail').decode('UTF8') , StyleRowDetailWrap    ); 
                row1.write(2, value.get('report_date') ,styleDate );
                row1.write(3, value.get('report').decode('UTF8')  ,styleRowDetail );
                i=i+1; 
                
                for sub in value.get('response') :
                    row1 = sheet1.row(i) ;
                    row1.write(0," "  );
                    text = "(" +  sub.get('risk_team').decode('UTF8') + " )   "   +  sub.get('result').decode('UTF8');
                    
                    row1.write(1, text ,StyleRowDetailWrap );
                    
             
                    i=i+1; 
                
                
        dirTempFile = gettempdir() + _os.sep + str('simpleReport5.xls');
        
        book.save(dirTempFile);  
        
        return dirTempFile;
        
    def exportToExcel(self,objectProject):
        
        book = Workbook();
        sheet1 = book.add_sheet('Sheet 1')
        sheet1.col(1).width = 256*20;
        sheet1.col(2).width = 256*80;
        sheet1.col(3).width = 256*10;
        sheet1.col(4).width = 256*20;
        
        default_book_style = book.default_style
        default_book_style.font.height = 20 * 36    # 36pt
        
        fnt = Font()
        fnt.name = 'Arial'
        fnt.colour_index = 4
        fnt.bold = True
        
        borders = Borders()
        borders.left = Borders.THIN
        borders.right = Borders.THIN
        borders.top = Borders.THIN
        borders.bottom = Borders.THIN
        
        pattern = Pattern();
        pattern.pattern = Pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = 23
        
        
        algn1 = Alignment();
        algn1.wrap = 1;
        #algn1.horz = Alignment.HORZ_CENTER
        #algn1.vert = Alignment.VERT_TOP
        
        alignHeader =  Alignment();
        alignHeader.horz = Alignment.HORZ_CENTER;
        
        alignTop =  Alignment();
        alignTop.vert = Alignment.VERT_TOP    
        print "export";
        if( objectProject):
            i=0;
           
            print "start" ;
            
            styleHead = XFStyle();
            styleHead.font = fnt;
            styleHead.borders = borders;
            styleHead.pattern = pattern;
            styleHead.alignment = alignHeader;
            
            row1 = sheet1.row(i) ;
            row1.write(0, ('risk id').decode('UTF8'),styleHead );
            sheet1.write_merge(i, i, 1, 2,  ('รายละเอียด').decode('UTF8')  ,styleHead  );
            
          #  row1.write(1, ('รายละเอียด').decode('UTF8'));
            
            row1.write(3, ('วันที่รายงาน').decode('UTF8'), styleHead );
            row1.write(4, ('หน่วยที่รายงาน').decode('UTF8'), styleHead );
            
            i=i+1; 
            
            
            style1 = XFStyle();
            style1.alignment = algn1;
            
            #style0 = xlwt.easyxf('font: name Times New Roman size 20, color-index black, bold on')
            
            
            for value in  objectProject:
                
                row1 = sheet1.row(i) ;
                
                styleRowDetail = XFStyle();
                styleRowDetail.borders = borders;
                styleRowDetail.alignment = alignTop;
                
                StyleRowDetailWrap = styleRowDetail ;
                StyleRowDetailWrap.alignment = algn1;
                
                styleDate = XFStyle()
                styleDate.num_format_str = 'DD-MM-YYYY'   ;   #'D-MMM-YY';
                styleDate.borders = borders;
                
                row1.write(0, value.get('risk_management_id'),styleRowDetail  );
                #row1.write(1, value.get('risk_detail').decode('UTF8') , style1);
                sheet1.write_merge(i, i, 1, 2,   value.get('risk_detail').decode('UTF8') , StyleRowDetailWrap    ); 
                row1.write(3, value.get('report_date') ,styleDate);
                row1.write(4, value.get('report').decode('UTF8') ,styleRowDetail );
                
                i=i+1; 
                row1 = sheet1.row(i) ;
                row1.write(0," "  );
                row1.write(1,('หน่วยที่เกี่ยวข้อง').decode('UTF8') ,styleHead      );
                sheet1.write_merge(i, i, 2, 3,('รายละเอียดการตอบ').decode('UTF8') , styleHead );
                i=i+1; 
                
                for sub in value.get('response') :
                    row1 = sheet1.row(i) ;
                    row1.write(0," "  );
                    row1.write(1,sub.get('risk_team').decode('UTF8') , styleRowDetail   );
                    sheet1.write_merge(i, i, 2, 3,sub.get('result').decode('UTF8') , StyleRowDetailWrap );
                
                    i=i+1; 
        
        dirTempFile = gettempdir() + _os.sep + str('simple.xls');
        print   dirTempFile;      
        book.save(dirTempFile);
        