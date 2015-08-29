class message_handler(object):
    def __init__(self, topic, pattern, answer_template):
        """
        Initiate message_handler object.
        :param topic: parent topic
        :param pattern: pattern to match the category
        :param answer_template: answer template the will be used to answer when the pattern is match
        :return: None
        """
        self.topic = topic
        self.pattern = pattern
        self.answer_template = answer_template




