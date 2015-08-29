# -*- coding: utf-8 -*-
from answer_template import answer_template
import codecs
import sys
import os
import site
import re
from BeautifulSoup import BeautifulSoup
import random

for site in site.getsitepackages():
    p = os.path.join(site,'xgoogle-master')
    if p not in sys.path:
        sys.path.append(p)
from xgoogle.search import GoogleSearch, SearchError
from xgoogle.browser import *
import wikipedia
# from browser import Browser, BrowserError

# from pygoogle import google
class avoiding_msg_movies(answer_template):
    def get(self, params=None):
        """
        gets the answer from the answer template
        :param params: msg = params[0], func = params[1]
        :return:
        returns the first template if is_random is false, otherwise returns random template
        """
        msg = (params[0] + " " +u"סרט ויקיפדיה").encode('utf-8')
        paranthesis_pattern= "[\(].*?[\)]"
        try:
            b = Browser()
            gs = GoogleSearch(msg)
            gs.results_per_page = 50
            results = gs.get_results()
            for res in results:
                # print res.title.replace('ynet','')
                try:
                    if (res.url is not None):
                        page = b.get_page(res.url)
                        soup = BeautifulSoup(page)
                        title = soup.find("title")
                        if (title is not None):
                            res = title.text.split('-')[0]
                            re.sub(paranthesis_pattern, "", res)
                            wikipedia.set_lang('He')
                            title = wikipedia.search(res)
                            if (len(title) == 0):
                                return u"לא מכיר את הסרט הזה"
                            wiki_summary = wikipedia.summary(title[0])
                            if (wiki_summary is None):
                                return title + "?"
                            paranthesis_values = re.findall(paranthesis_pattern,wiki_summary)
                            english_name = ""
                            for value in paranthesis_values:
                                if (u'באנגלית' in value):
                                    english_name = re.sub(r'[^a-zA-Z ]', '', value.encode('utf-8'))
                                    # english_name = value
                            if (english_name == ""):
                                return u"וואלה לא ראיתי את הסרט הזה, הביקורות עליו טובות?"
                            query = 'www.imdb.com:' + english_name
                            gs = GoogleSearch(query)
                            gs.results_per_page = 50
                            results = gs.get_results()
                            for imdb_res in results:
                                if (imdb_res.url is not None):
                                    page = b.get_page(imdb_res.url)
                                    soup = BeautifulSoup(page)
                                    rating = soup.find("span", {"class":"rating"})
                                    if (rating is not None):
                                        rate = float(rating.next)
                                        return self.get_response_by_rate(rate)


                    break

                except Exception as e:
                    print(e)
                    return u"לא מכיר את הסרט הזה"
                return u"לא מכיר את הסרט הזה"
        except SearchError, e:
            print "Search failed: %s" % e

    def get_response_by_rate(self,rate):
        if (rate > 7.5):
            templates = self.get_templates("good_movies")
            return random.choice(templates)
        if (rate < 6.5):
            templates = self.get_templates("terrible_movies")
            return random.choice(templates)
        #terrible
        templates = self.get_templates("medium_movies")
        return random.choice(templates)


    def get_templates(self,file_name):
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Templates",file_name)
        f = codecs.open(path, 'r', encoding='utf8')
        templates = f.readlines()
        return templates




