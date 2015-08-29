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


class politics_topic(topic):
    def __init__(self):
        super(politics_topic, self).__init__(classifier.politics_topic)
        super(politics_topic, self).init_from_xml(classifier.politics_topic + ".xml")
        self.avoiding_msg = avoiding_msg_ynet()

    def get_avoiding_message(self, msg):
        return self.avoiding_msg.get([msg])

