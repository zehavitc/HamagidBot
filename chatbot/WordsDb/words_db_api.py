# -*- coding: utf-8 -*-
import sqlite3 as lite
import os

class words_db_api(object):
    def __init__(self):
        path = os.path.dirname(os.path.abspath(__file__))
        self.con = lite.connect(os.path.join(path,'words.sqlite3'))
        self.con.text_factory = lambda x: unicode(x, 'utf-8', 'replace')

    def get_translation(self,words):
        row = self.con.execute("SELECT translation FROM Words WHERE Word=? ", (words,)).fetchall()
        if row is None or len(row) == 0:
            return []
        rowStr = ''.join(w.strip() for w in row[0])
        return rowStr.split(',')


# w = words_db_api()
# print(w.get_translation(u"מה"))
