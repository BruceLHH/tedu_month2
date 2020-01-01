
class ListHelper:
    """
    list helper
    """
    @staticmethod
    def find_all_enemy(list_target,fun_condition):
        """

        :param list_target:
        :param fun_condition:
        :return:
        """
        for item in list_target:
            if fun_condition(item):
                yield item
    @staticmethod
    def find__count(list_target,fun_condition):
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
    @staticmethod
    def caculate_sum(list_target,fun_condition):
        sum = 0
        for item in list_target:
            sum += fun_condition(item)
        return sum
    @staticmethod
    def filter(list_target,fun_condition):
        list_res = []
        for item in list_target:
            list_res.append(fun_condition(item))
        return list_res
    @staticmethod
    def filter_yield(list_target, fun_condition):
        for item in list_target:
            yield fun_condition(item)
    @staticmethod
    def get_max_value(list_target,fun_condition):
        max_value = list_target[0]
        for item in list_target:
            if fun_condition(max_value)< fun_condition(item):
                max_value = item
        return max_value
    ### def fun_condition():
    ##      return item.hp  /item.atk
    @staticmethod
    def get_min_value(list_target, fun_condition):
        min_value = list_target[0]
        for item in list_target:
            if fun_condition(min_value) > fun_condition(item):
                min_value = item
        return min_value
    @staticmethod
    def sort_ascending(list_target,fun_condition):
        """

        :param list_target:
        :param fun_condition: function(arg)
        :return: None
        """
        for i in range(len(list_target) - 1):
            temp = i
            for j in range(i+1,len(list_target)):
                if fun_condition(list_target[temp]) > fun_condition(list_target[j]):
                    temp = j
            if (i != temp):
                list_target[temp],list_target[i] = list_target[i],list_target[temp]

    @staticmethod
    def sort_decend(list_target, fun_condition):
        """

        :param list_target:
        :param fun_condition: function(arg)
        :return: None
        """
        for i in range(len(list_target) - 1):
            temp = i
            for j in range(i + 1, len(list_target)):
                if fun_condition(list_target[temp]) < fun_condition(list_target[j]):
                    temp = j
            if (i != temp):
                list_target[temp], list_target[i] = list_target[i], list_target[temp]
    @staticmethod
    def del_enemy(list_target,fun_condition):
        for index in range(len(list_target)-1,-1,-1):
            if fun_condition(list_target[index]):
                del list_target[index]
