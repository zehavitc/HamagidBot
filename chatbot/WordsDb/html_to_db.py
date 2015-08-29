import sqlite3 as lite
import re
import string
import xml
# -*- coding: utf-8 -*-

class ConvertHtmlToSqlite(object):
    def __init__(self):
        self.parenthesisRe = re.compile(r'\([^)]*\)')
        self.tagRe = re.compile(r'(\s)*<[^>]+>')
        self.characters = list('\xd7\xa4\xd7\x9d\xd7\x9f\xd7\x95\xd7\x98\xd7\x90\xd7\xa8\xd7\xa7\xd7\xa3\xd7\x9a\xd7\x9c\xd7\x97\xd7\x99\xd7\xa2\xd7\x9b\xd7\x92\xd7\x93\xd7\xa9\xd7\xa5\xd7\xaa\xd7\xa6\xd7\x9e\xd7\xa0\xd7\x94\xd7\x91\xd7\xa1\xd7\x96,; \"-')
        self.con = lite.connect('./words.sqlite3')
        self.con.execute(("CREATE TABLE Words(Word VARCHAR(250), Translation VARCHAR(250))"))
        self.con.text_factory = lambda x: unicode(x, 'utf-8', 'replace')

    def convert(self):
        with open('./babylon_hebrew.html') as f:
            word = None
            # chartToStrip = string.ascii_lowercase + string.ascii_uppercase + string.whitespace + '<'+'>' +r'\'
            translation = None
            for line in f:
                if '<idx:orth>' in line:
                    word = self.remove_tags(line)
                    continue
                if '<p><ul><li><blockquote>' in line:
                    translation = self.remove_tags(line)
                if word is not None and translation is not None:
                    if translation != "":
                        self.WriteToDb(word, translation)
                    word = None
                    translation = None
        self.con.commit()

    def remove_tags(self, text):
        text = self.tagRe.sub('', text)
        text = self.parenthesisRe.sub('', text)
        text = ''.join(c for c in text if c in self.characters)
        text = unicode(text, 'utf-8', 'replace')
        text = text.replace(u'\ufffd', '')
        return text
        # return text

    def WriteToDb(self, word, translation):
        self.con.execute("INSERT INTO Words VALUES(?,?)", (word, translation))


c = ConvertHtmlToSqlite()
c.convert()