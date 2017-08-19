# -*- coding: utf-8 -*-
import requests,json
import urllib


class Util(object):
    URL_LINE_NOTIFY = "https://notify-api.line.me/api/notify"
    LINE_HEADERS = {
            'Content-Type':'application/x-www-form-urlencoded'
        }
    MESSAGE_FIELD = {'message' : ''}
    def __init__(self):
        pass
    
    def calllinenotify(self, LINE_ACCESS_TOKEN, message = ""):      
        self.LINE_HEADERS['Authorization'] = 'Bearer ' + LINE_ACCESS_TOKEN
        self.MESSAGE_FIELD['message'] = message
        
        session = requests.Session() 
        a=session.post(
            url= self.URL_LINE_NOTIFY,
            headers= self.LINE_HEADERS
            ,data=self.MESSAGE_FIELD
            )
        value = json.loads(str(a.text))
        print(  value)
        
        print('Response HTTP Status Code: {status_code}'.format( status_code=value.get('status')))
        
"""
u = Util()

formattype = "\nระดับ   : {level} \nรายละเอียด : {detail}"

message = 'ไฟดับ 2 ครั้ง ทำให้เข้าใช้งาน net work ไม่ได้ส่งผลให้เข้า โปรแกรม ระบบ XP ทำงานไม่ได้ด้วย'
u.calllinenotify(LINE_ACCESS_TOKEN="WloP07XPXvCfSdIUBpY7fBMavQHI2haPM9wHVTK6QSU" ,
                  message=formattype.format(level='E', detail = message))


message = 'test'
u.calllinenotify(LINE_ACCESS_TOKEN="WloP07XPXvCfSdIUBpY7fBMavQHI2haPM9wHVTK6QSU" , 
                 message=formattype.format(level='H', detail = message))
"""
#pip install -U requests[security]
#sudo pip install -U requests[security]
#yum install libffi-devel python-cffi
#https://stackoverflow.com/questions/22252397/importerror-no-module-named-mysqldb

#pip install cffi enum34 ethtool pcp perf ply pycparser pycurl pyparsing urlgrabber urwid -y


#requests.exceptions.SSLError: HTTPSConnectionPool(host='notify-api.line.me', port=443): Max retries exceeded with url: /api/notify (Caused by SSLError(SSLError("bad handshake: Error([('SSL routines', 'SSL3_GET_SERVER_CERTIFICATE', 'certificate verify failed')],)",),))