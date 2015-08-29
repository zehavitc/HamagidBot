# -*- coding: utf-8 -*-
import codecs
import os
from hebrew_aiml.answer_template import answer_template
from hebrew_aiml.avoiding_msg_ynet import avoiding_msg_ynet
from hebrew_aiml.message_handler import message_handler
from hebrew_aiml.pattern import pattern
from .topic import topic
from .wiki_helper import *
from .xml_helper import parse_patterns_xml
from topic_classifier.topic_classifier import classifier


class sport_topic(topic):
    def __init__(self):
        super(sport_topic, self).__init__(classifier.sport_topic)
        super(sport_topic, self).init_from_xml(classifier.sport_topic + ".xml")
        self.avoiding_msg = avoiding_msg_ynet()

    def get_avoiding_message(self, msg):
        return self.avoiding_msg.get([msg])

