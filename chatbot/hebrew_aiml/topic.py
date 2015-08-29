import codecs
import os
from hebrew_aiml.answer_template import answer_template
from hebrew_aiml.avoiding_msg_wiki import avoiding_msg_wiki
from hebrew_aiml.message_handler import message_handler
from hebrew_aiml.pattern import pattern
from .xml_helper import parse_patterns_xml


class topic(object):
    def __init__(self, id):
        """
        Initiate topic object
        :param id: int (unique)
        :return:None
        """
        self.message_handlers = []
        self.id = id

    def get_avoiding_message(self, msg):
        """
        Get avoiding message if the message does not match any of the patterns
        :param msg:  The message to response to
        :return: return avoiding msg based on msg
        """
        pass

    def init_from_xml(self,xml_file_name):
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Templates", xml_file_name)
        patterns = parse_patterns_xml(path)
        for pattern_xml in patterns:
            self.message_handlers.append(
                message_handler(self, pattern(pattern_xml[0], False)
                                , answer_template(pattern_xml[1])))
