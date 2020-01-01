
"""

"""
class List_helper:
    """
    list helper
    """
    @staticmethod
    def find_number(list_target,func_condition):
        """

        :param list_target:
        :param func_condition:
        :return:
        """
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def count_number(list_target, func_condition):
        """

        :param list_target:
        :param func_condition:
        :return:
        """
        count = 0
        for item in list_target:
            if func_condition(item):
                count += 1
        return count