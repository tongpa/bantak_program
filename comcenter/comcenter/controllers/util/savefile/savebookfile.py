import os as _os;
import time;
import random;
from time import gmtime, strftime
class SaveBookFile(object):
    
    def __init__(self):
        pass;
    
     
    def save(self,file,path,book_type ):
        
        print "-----save file";
        self.newFileName = None;
        try:
            print path;
            self.checkPath(path);
            if file is not None:
                
                self.fileName = file.filename; 
                print self.fileName;
                print "-----*****";
                self.data = file.file.read();
                print self.data;
                print "-----*****";
                self.name, self.fileExt = _os.path.splitext(self.fileName);
                
                print self.name;
                print self.fileExt;
                print "-----*****";
                
                self.newFileName = book_type + "_"  + self.getFileName() +  self.fileExt;
                target_file_name = _os.path.join(_os.getcwd(), path,self.newFileName);
               
                
                print "New file name : " + str(target_file_name);
                
                writefile = open(target_file_name, 'wb');
                writefile.write(self.data);
                writefile.close();
                 
                
        
        except Exception: 
            print "error file";
            
        return self.newFileName;
    
    def checkPath(self,path):
        if not _os.path.exists(path):
            print "path not exists";
            _os.makedirs(path);            
        pass;
    
    def getFileName(self ):
        
        return time.strftime('%Y%m%d%H%M%S') + "_" + str(random.randrange(10001, 99999, 5));
         
         
        #print strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        #target_file_name = _os.path.join(_os.getcwd(), path,upload_file.filename)
 
 