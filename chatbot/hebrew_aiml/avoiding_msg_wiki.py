# -*- coding: utf-8 -*-

__author__ = 'zehavitc'

import random

import wikipedia

from answer_template import answer_template
from .patterns_helper import ngrams


class avoiding_msg_wiki(answer_template):
    def get(self, params=None):
        """
        gets the answer from the answer template
        :param params: msg = params[0], func = params[1]
        :return:
        returns the first template if is_random is false, otherwise returns random template
        """
        msg = params[0]
        topic = self.get_topic_wiki(msg)
        if self.is_random:
            answer = random.choice(self.li)
        else:
            answer = self.li[0]
        if len(params) > 1:
            func = params[1]
            topic = func(topic)
        try:
            #r = answer.replace(u'*'.encode('utf-8'), topic.encode('utf-8'))
            r = answer.replace(u'*', topic)
        except Exception as e:
            print(e)
        return r



    def get_topic_wiki(self, msg):
        bigrams = ngrams(msg, 2)
        unigrams = ngrams(msg,1)
        msg_ngrams =  bigrams + unigrams
        # msg_ngrams += msg.split()
        lens = []
        wikipedia.set_lang('He')
        gram_to_values = {}
        for gram in msg_ngrams:
            value = wikipedia.search(gram, 1, True)
            if len(value[0]) == 0:
                lens.append(0)
            else:
                try:
                    page_len = len(wikipedia.page(value[0][0]).content)
                    lens.append(page_len)
                except:
                    lens.append(0)

        max_len = max(lens)
        idx = [i for i, x in enumerate(lens) if x == max_len]
        topic = msg_ngrams[random.choice(idx)]
        return topic

        # a = answer_template_wiki(True,["אני לא רוצה לדבר על *", "אני מעדיף שלא לדבר על *", "* זה ממש משעמם בוא נדבר על משהו אחר", "* זה לחנונים, אין לך משהו יותר טוב לדבר עליו?", "עזוב אותי מ*, מה חדש?", " לא כל כך מעניין אותי לדבר על *"])
        #a.get_topic_wiki('אורן חזן')