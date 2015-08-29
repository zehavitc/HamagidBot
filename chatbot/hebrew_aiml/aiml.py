# -*- coding: utf-8 -*-
import exceptions
import wikipedia
import random
import os
from topic_classifier.topic_classifier import classifier



class aiml(object):
    def __init__(self, basic_topic, topics):
        """
        initiate the hebrew_aiml object
        :param basic_topic: topic to match first
        :param topics: list of known topics the chat bot can use to answer the user
        :return: None
        """
        self.current_topic = topics[0]
        self.basic_topic = basic_topic
        self.topics = topics
        self.classifier = classifier()

    def find_topic(self,msg):
        """
        finds the conversation topic based on the current msg the user sent.
        :param msg:string, required
        :return: no return value. the function updates the current_topic field.
        """
        topic_id = self.classifier.classify(msg)
        for topic in self.topics:
            if topic_id == topic.id:
                return topic
        raise Exception("aiml - classifier topic does not match given topics")

    def respond(self,msg):
        """
        implements the respond logic of the chat bot
        :param msg:string, required
        :return: return the chat bot response to the given msg
        """


        #basic topic
        for msg_handler in self.basic_topic.message_handlers:
            if msg_handler.pattern.is_match(msg):
                return msg_handler.answer_template.get(msg)
        #get topic and response
        topic = self.find_topic(msg)
        if not (topic is None):
            self.current_topic = topic
        else:
            raise Exception("find topic - None value is not expected")

        for msg_handler in self.current_topic.message_handlers:
            if msg_handler.pattern.is_match(msg):
                return msg_handler.answer_template.get(msg)
        return self.current_topic.get_avoiding_message(msg)








