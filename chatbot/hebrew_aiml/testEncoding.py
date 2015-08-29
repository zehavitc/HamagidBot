__author__ = 'zehavitc'
# -*- coding: utf-8 -*-

r = "אני לא רוצה לדבר על *"
b= u'ישראל מפלגות'
a= u'*'
print(r.replace(a.encode('utf-8'),b.encode('utf-8')))
