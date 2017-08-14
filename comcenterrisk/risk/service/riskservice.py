# -*- coding: utf-8 -*-

from risk.lib.util import Util
from tgext.pluggable import app_model

class RiskService(object):
    def __init__ (self):
        self.util = Util()
        pass
    
    
    def notifyByLevel(self, risk):
        if risk and risk.risk_level.alert_report == 1 :
            LINE_ACCESS_TOKEN = "WloP07XPXvCfSdIUBpY7fBMavQHI2haPM9wHVTK6QSU"
            
            formattype = "\nระดับ   : {level} \nรายละเอียด : {detail}"
            level = risk.risk_level.description
            message = risk.detail
            
            self.util.calllinenotify(LINE_ACCESS_TOKEN=LINE_ACCESS_TOKEN ,
                  message=formattype.format(level=level, detail = message))
        
            
            
            