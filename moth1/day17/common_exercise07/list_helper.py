"""

list helper
"""
class List_helper:
    """
    list helper
    """
    @staticmethod
    def get_skill(list_skill,fun_condition):
        """
        get one skill.
        :param list_skill: skill list of give
        :param fun_condition: judge condition
        :return: skill objcetion
        """
        for item in list_skill:
            if fun_condition(item):
                return item