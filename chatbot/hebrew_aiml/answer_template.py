import exceptions
import random

class answer_template(object):
    def __init__(self, li = None):
        """
        Initiate the answer_template object
        :param li: list of templates for response
        :return:None
        """
        self.li = li


    def get(self, params=None):
        """
        gets the answer from the answer template
        :param params: optional parameters to get respond that fits the original message
        :return:
        returns the first template if is_random is false, otherwise returns random template
        """
        return random.choice(self.li)

