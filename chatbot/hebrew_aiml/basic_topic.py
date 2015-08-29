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


class basic_topic(topic):
    def __init__(self):
        super(basic_topic, self).__init__("basic")
        super(basic_topic, self).init_from_xml("basic.xml")

    def get_avoiding_message(self, msg):
        raise Exception("basic topic - method not implemented")
