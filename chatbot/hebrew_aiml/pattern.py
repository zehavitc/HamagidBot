# -*- coding: utf-8 -*-
from patterns_helper import ngrams
from WordsDb import words_db_api
import re

class pattern(object):
    def __init__(self, templates, use_synonyms=True):
        """
        Initiate pattern object
        :param templates: list of templates to match
        :param use_synonyms: use synonyms to create more templates
        :return: None
        """
        self.templates = templates
        if not use_synonyms:
            return
        res = []
        words_api = words_db_api.words_db_api()
        for template in templates:
            print(template.split(u'*'))
            sub_templates = [w.strip() for w in template.split(u'*')]
            for sub_template in sub_templates:
                print(sub_template)
                for i in list(reversed(range(1, 3))):
                    grams = ngrams(sub_template, i)
                    for ngram in grams:
                        # print(ngram)
                        trans = words_api.get_translation(ngram)
                        for translation in trans:
                            if len(translation.split()) <= 2 and translation != "":
                                res += sub_template.replace(ngram, translation)
        self.templates += res


    def is_match(self, msg):
        """
        check if msg is match to pattern
        :param msg: string, required
        :return: true\ false
        """
        for template in self.templates:
            try:
                if re.match(template, msg):
                    return True
            except Exception as e:
                print(e)
        return False




# h = u'מבחן'
# print(h)
# p = pattern([u'מה המצב אחי'])
# print(p.is_match(u'איך המצב אחי'))