
class List_helper:
    """
    list helper
    """
    @staticmethod
    def find_enemy_info(list_target,fun_condition):
        """

        :param list_target:
        :param fun_condition:
        :return:
        """
        for item in list_target:
            if fun_condition(item):
                yield item
    @staticmethod
    def find_enemy_count(list_target,fun_condition):
        """

        :param fun_condition:
        :return:
        """
        count = 0
        for item in list_target:
            if fun_condition(item):
                count += 1
        return count
    @staticmethod
    def is_exist(list_target,fun_condition):
        """

        :param fun_condition:
        :return: bool
        """
        for item in list_target:
            if fun_condition(item):
                return True
        return False
