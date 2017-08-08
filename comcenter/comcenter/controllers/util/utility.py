# coding=utf8
from datetime import datetime,date,time,timedelta;
import calendar;
from math import floor
class Utility(object):
    month = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม'];
    
    def __init__(self):
        #self.time_format = '%Y-%m-%dT%H:%M:%S';
        self.time_format = '%d/%m/%Y';
        self.timeT_format = '%Y-%m-%dT%H:%M:%S';
        
        self.defaultyear = int(datetime.now().strftime("%Y")) + int(543)
        self.startyear = 2554;
        self.stopyear =   self.defaultyear + int(2)
        
        pass;
    def sumLevel(self,list,level):
        if(list and level):
            result = 0;
            for v in list:
                result = result + v.get(level);
                 
            
            return result;
            
        return '0';
    def changeValueZero(self,value):
        if (value ):
            if(value == 0):
                return '';
            else:
                return value;
        else:
            return '';
    def getMonthThai(self,value):
        return self.month[value-1]; 
    def ifNull(self,value,data):
        if(value):
            return value;
        else:
            return data;
    
    def numValue(self,value):
        if(value is None):
            return 0;
        return value;
                
    def isValue(self,data):
        if(data):
            if(len(str(data).strip()) != 0):
                if(str(data).strip() != '0'):
                    if(str(data).strip() != '*'):
                        return data;
                    return None;
                else:
                    return None;
            else:
                return None;
        else:
            return None;
        
    def valueNull(self,data):
        data = self.isValue(data);
        if(data is None):
            data ='';
        return data;
        
        
    def getArrayComma(self,data):
        if(data):
            return data.split(',');
        else:
            return [];
    def spitStringDate(self,data):
        if(data):
            return data.split('T')[0];
        else : 
            return data;     
    def convertStringToDate(self,data ):
        if(data):
            if ("T" in data) :
                return datetime.strptime(data, self.timeT_format);
            else:
                return datetime.strptime(data, self.time_format);
        else:
            return data;
    
    def convertStringDateToString(self,date,format):
        if(date):
                date = datetime.strptime(date, self.time_format);
        else: 
                date = datetime.now();
        return date.strftime(format);
        
    
    def last_day_of_month(self,date):
        if date.month == 12:
            return date.replace(day=31);
        return date.replace(month=date.month+1, day=1) - timedelta(days=1);
    
    def monthInYM(self,ym):
        if(ym and len(ym)== 7 and  ('-' in ym) ):
            value = ym.split('-') ;
            return int(value[1]);
        else :
            return ym;
        
    def buddhistToAD(self,bh):
        if(bh):
            return int(bh)-543;
        return bh;
    
    def checkFlowRiskStatus(self,value):
        value = int(value);
        if(value == 1):
            return 2;
        if(value ==2):
            return 3;
        if(value == 3):
            return 4;
        if(value == 4):
            return 5;
    
    def getmonthrange(self,year,month):
        print calendar.monthrange(year,month)[1];
        

    def getRangeYear(self,year):
        listYear=[];
         
        if year is None:
            year = self.defaultyear;
        for years in range(self.startyear ,self.stopyear) :            
            if(year and ( str(year) == str(years)) ):
                listYear.append({'id':years,'value':years});
            else:
                listYear.append({'id':years,'value':years});
        return listYear;
    
    def convertDateToString(self,date,format): #2012-10-17 00:00:00
       
        if date:            
            return date.strftime(format); #"%d/%m/%Y");
        else : 
            return "";
    
    def floorValue(self, value):
        return floor(value)
    
    def checkCriteria(self,firstValue,expression,secondValue):
        if '=' == expression:
            #print "%s =(%s) %s"   %(firstValue, expression, secondValue)
            return firstValue == secondValue
        elif '<' == expression:
            #print "%s <(%s) %s"  %(firstValue, expression, secondValue)
            return firstValue < secondValue
        elif '<=' == expression:
            #print "%s <= %s"  %(firstValue, secondValue)
            return firstValue <= secondValue
        elif '>' == expression:
            #print "%s > %s"  %(firstValue, secondValue)
            return firstValue > secondValue
        elif '>=' == expression:
            #print "%s >= %s"  %(firstValue, secondValue)
            return firstValue >= secondValue
        elif '!=' == expression:
            #print "%s != %s"  %(firstValue, secondValue)
            return firstValue != secondValue
        
        #print "except : %s %s %s"  %(firstValue,expression, secondValue)
        return False
    def calFiscalYear(self,month,year):
        
        if month is not None and int(month) >=10:
            return int(year) +1
        return year
         

util = Utility();
#print util.checkCriteria('28', '>=','24')
#print util.calFiscalYear(10, 2559)
 
#print util.getArrayComma('23,33,44,55,22');
#util.getmonthrange(2011, 4);
#print util.spitStringDate("2011-11-01T00:00:00");
#print str("87").split(',');
#d = util.isValue( 0 );
#print d;
"""
print util.buddhistToAD('2554');
print util.getMonthThai(3);
print util.monthInYM('2011-03');
a= [27.27,42.86,    50,    23.81    ,31.25,    53.33,    46.67,    16,    26.19,     26.66 ,    18.75,    21.74,    51.72];
a.sort();
for i in range(len(a)):
    print i,a[i];
    
b = [];
b.append({'a':27.27,'name':'test1','id':1,'sorted':0});
b.append({ 'a':50,'name':'test2','id':2,'sorted':0});
b.append({ 'a':23.81,'name':'test3','id':3,'sorted':0});
b.sort();


for i in range(len(b)):
    dd = b[i];
    dd['sorted'] = i; 
    print i,dd;

print max(a);    

host = "110.77.138.136:8282";
port = ":8282";
print host.rstrip(port);
dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print dt.strftime("%A, %d. %B %Y %I:%M%p")
print dt.strftime("%d/%m/%Y")
"""

#dates = datetime.now();

#dt = int(dates.strftime("%Y")) + int(543)

#dtm = dates.strftime("%m")
#print dt;
#print dtm
 
