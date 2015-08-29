# -*- coding: utf-8 -*-
import codecs
import os
from hebrew_aiml.answer_template import answer_template
from hebrew_aiml.avoiding_msg_wiki import avoiding_msg_wiki
from hebrew_aiml.message_handler import message_handler
from hebrew_aiml.pattern import pattern
from .topic import topic
from .wiki_helper import *
from .xml_helper import parse_patterns_xml
from topic_classifier.topic_classifier import classifier


class blather_topic(topic):
    def __init__(self):
        super(blather_topic, self).__init__(classifier.blather_topic)
        super(blather_topic, self).init_from_xml(classifier.blather_topic + ".xml")

    def get_avoiding_message(self, msg):
        try:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Templates", "avoiding_templates")
            f = codecs.open(path, 'r', encoding='utf8')
            templates = f.readlines()
            return avoiding_msg_wiki(templates).get([msg, get_category])
        except Exception as inst:
            print(inst)
