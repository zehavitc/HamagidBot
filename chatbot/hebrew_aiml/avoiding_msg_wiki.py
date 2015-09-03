# -*- coding: utf-8 -*-

__author__ = 'zehavitc'

import random
import wikipedia
from answer_template import answer_template
from .patterns_helper import ngrams
import site
import os
import sys

for site in site.getsitepackages():
    p = os.path.join(site, 'xgoogle-master')
    if p not in sys.path:
        sys.path.append(p)
from xgoogle.search import GoogleSearch, SearchError
from xgoogle.browser import *


class avoiding_msg_wiki(answer_template):
    default_topic = u"זה"
    words_to_avoid = [u'אני', u'את', u'אתה', u'אתם', u'אתן', u'היא', u'הוא', u'מה', u'אנחנו', u'אנו', u'הם', u'הן',
                      u'לך', u'בשבילך', u'עבורך', u'בשבילכם', u'בשבילן']

    def get(self, params=None):
        """
        gets the answer from the answer template
        :param params: msg = params[0], func = params[1]
        :return:
        returns the first template if is_random is false, otherwise returns random template
        """
        msg = params[0]
        topic = self.get_topic_wiki(msg)
        answer = random.choice(self.li)
        if len(params) > 1:
            func = params[1]
            if (topic != self.default_topic):
                topic = func(topic)
        try:
            # r = answer.replace(u'*'.encode('utf-8'), topic.encode('utf-8'))
            r = answer.replace(u'*', topic)
        except Exception as e:
            print(e)
        return r

    def get_topic_wiki(self, msg):
        b = Browser()
        wikipedia.set_lang('He')
        for word in self.words_to_avoid:
            msg = msg.replace(word, "")
        num_of_words = len(msg.split())
        article_lens = {}
        categories = []
        for j in list(reversed(range(2))):
            for i in list(reversed(range(1, num_of_words + 1))):
                msg_ngrams = ngrams(msg, i)
                article_lens = {}
                categories = {}
                for gram in msg_ngrams:
                    value = wikipedia.search(gram, 1, True)
                    if len(value[0]) == 0:
                        continue
                    else:
                        try:
                            # first loop searches for exact match and the second one allows suggestions
                            if value[0][0] != gram and j: continue
                            page_len = len(wikipedia.page(value[0][0]).content)
                            article_lens[gram] = page_len
                        except:
                            # maybe The gram is wiki category
                            try:
                                category_link = ("https://he.wikipedia.org/wiki/" + u"קטגוריה" + u":" + gram).encode(
                                    'utf-8')
                                category_page = b.get_page(category_link)
                                categories[gram] = len(category_page)
                            except Exception as e:
                                print(e)
                                continue
                if len(article_lens) != 0:
                    max_len = max(article_lens.iterkeys(), key=(lambda key: article_lens[key]))
                    max_article = [key for key, value in article_lens.iteritems() if value == article_lens[max_len]]
                    return random.choice(max_article)
                if len(categories) != 0:
                    max_len = max(categories.iterkeys(), key=(lambda key: categories[key]))
                    max_categories = [key for key, value in categories.iteritems() if value == categories[max_len]]
                    return random.choice(max_categories)
        return self.default_topic


            # a = answer_template_wiki(True,["אני לא רוצה לדבר על *", "אני מעדיף שלא לדבר על *", "* זה ממש משעמם בוא נדבר על משהו אחר", "* זה לחנונים, אין לך משהו יותר טוב לדבר עליו?", "עזוב אותי מ*, מה חדש?", " לא כל כך מעניין אותי לדבר על *"])
            # a.get_topic_wiki('אורן חזן')
