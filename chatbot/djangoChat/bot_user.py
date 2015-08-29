# -*- coding: utf-8 -*-
from hebrew_aiml.aiml import aiml
from hebrew_aiml.basic_topic import basic_topic
from hebrew_aiml.sport_topic import sport_topic
from hebrew_aiml.blather_topic import blather_topic
from hebrew_aiml.movies_topic import movies_topic

from hebrew_aiml.politics_topic import politics_topic


import time


class bot(object):
    def __init__(self):
        self.name = "Hamagid"
        self.aiml = aiml(basic_topic(),[sport_topic(),blather_topic(),movies_topic(),politics_topic()])

    def get_response(self, msg):
        r = self.aiml.respond(msg)
        return r





