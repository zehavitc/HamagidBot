# -*- coding: utf-8 -*-
from answer_template import answer_template
import sys
import os
import site
from BeautifulSoup import BeautifulSoup
for site in site.getsitepackages():
    p = os.path.join(site,'xgoogle-master')
    if p not in sys.path:
        sys.path.append(p)
from xgoogle.search import GoogleSearch, SearchError
from xgoogle.browser import *
# from browser import Browser, BrowserError

# from pygoogle import google
class avoiding_msg_ynet(answer_template):

    def find_between(self, s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ""

    def get(self, params=None):
        """
        gets the answer from the answer template
        :param params: msg = params[0], func = params[1]
        :return:
        returns the first template if is_random is false, otherwise returns random template
        """
        ynet_sections = [u"חדשות",u"כלכלה",u"ספורט",u"תרבות",u"רכילות",u"דיגיטל",u"בריאות",u"יהדות",u"חופש",u"רכב",u"אוכל",u"צרכנות",u"יחסים",u"mynet",u"מדע",u"לימודים",u"קניות",u"קהילות"]
        msg = ('ynet.co.il:'+params[0]).encode('utf-8')
        try:
            b = Browser()
            gs = GoogleSearch(msg,lang='he',tld="co.il")
            gs.results_per_page = 50
            results = gs.get_results()
            for res in results:
                try:
                    if (res.url is not None):
                        page = b.get_page(res.url)
                        soup = BeautifulSoup(page)
                        title = soup.find("title")
                        if (title is not None):
                            if ('&quot;' in title.text):
                                return self.find_between(title.text,'&quot;','&quot;')
                            res = title.text.split('-')[0].replace('ynet','').strip('"')
                            if ':' in res:
                                res = res.split(':')[1].strip('"')
                            res = res.strip()
                            if res == u'' or res in ynet_sections: continue
                            else: return res
                except:
                    continue
            return "?"
        except SearchError, e:
            return "?"



#a = avoiding_msg_ynet(None,None)
# a.get(["ynet.co.il:האם טביב ימכור את הקבוצה?"])
# res = a.get(["ynet.co.il:האם ביבי ימכור את המדינה?"])
#Sa.get(["ynet.co.il:מה יהיה עם הגז?"])
#a.get(["seret.co.il:המרגלת"])

#a = avoiding_msg_ynet()
#a.test_browser()
# a.get(["האם אלי טביב ימכור את הקבוצה?"])
#a.get(["ynet.co.il:איזה גרוע ביבי הא?"])