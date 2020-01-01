"""
    2048 game core controller
eg: __map = [[3,0,5,0,3,0],
              [3,5,5,0,3,0],
              [3,0,5,4,3,0],
              [2,0,6,7,3,0]]
"""
from model import *
import random
class GameCoreController:
    """
    game manager controller
    """
    def __init__(self):
        """
        get game data
        """
        self.__map = [[3,0,5,0,3,0],
              [3,5,5,0,3,0],
              [3,0,5,4,3,0],
              [2,0,6,7,3,0],
              [3, 0, 5, 4, 3, 0],
              [2, 0, 6, 7, 3, 0],
                      ]
        self.__empty_site_list = []
            #GameModel()
    @property #read
    def map(self):
        return self.__map
    def __zero_to_tail(self,list_merge):
        """
        move zero to the tail of list
        :param list_merge: the line want to move element
        :return:
        """
        for index in range(-1, -len(list_merge) - 1, -1):
            if list_merge[index] == 0:
                del list_merge[index]
                list_merge.append(0)
    def __merge_common_number(self,list_merge):
        """
        merge common element and move to left
        :param list_merge: line
        :return:
        """
        self.__zero_to_tail(list_merge)
        for index in range(len(list_merge) - 1):
            if list_merge[index] == list_merge[index + 1]:
                list_merge[index] += list_merge[index + 1]
                del list_merge[index + 1]
                list_merge.append(0)
    def __move_left_map(self):
        """
        merge element and move to left
        :return:
        """
        for line in self.__map:
            self.__merge_common_number(line)
    def __move_right_map(self):
        """
        1.reverse
        2.merge element and move to left,
        3.reverse
        :return:
        """
        for line in self.__map:
            line.reverse()
            self.__merge_common_number(line)
            line.reverse()
    def __map_transform(self):
        """
        transform map
        :return:
        """
        for row in range(len(self.__map)):
            for col in range(row):
                self.__map[row][col],self.__map[col][row] = self.__map[col][row],self.__map[row][col]
    def __move_up_map(self):
        """
        1. transform map
        2. merge element and move to left,
        3. transform map to return to the original shape
        :return:
        """
        self.__map_transform()
        self.__move_left_map()
        self.__map_transform()
    def __move_down_map(self):
        """
        1. transform map
        2. merge element and move to right,
        3. transform map to return to the original shape
        :return:
        """
        self.__map_transform()
        self.__move_right_map()
        self.__map_transform()

    def move(self,direction):
        """

        :param direction:
        :return:
        """
        if direction == DirectionModel.DOWM:
            self.__move_down_map()
        elif direction == DirectionModel.UP:
            self.__move_up_map()
        elif direction == DirectionModel.LEFT:
            self.__move_left_map()
        elif direction == DirectionModel.RIGHT:
            self.__move_right_map()
    def generate_random_number(self):
        """
        1. find a empty site
        2. generate a random number
        3. insert the number in a random empty site
        :return:
        """
        self.__generate_empty_site()
        if len(self.__empty_site_list) == 0:
            return
        gene_random_number=4 if random.randint(1,10) == 1 else 2
        self.__insert_number(gene_random_number)
    def __insert_number(self, gene_random_number):
        site_ = random.choice(self.__empty_site_list)
        self.__map[site_.index_r][site_.index_c] = gene_random_number
        self.__empty_site_list.remove(site_)
    def __generate_empty_site(self):
        self.__empty_site_list.clear()
        for index_r in range(len(self.__map)):
            for index_c in range(len(self.__map[index_r])):
                if self.__map[index_c][index_r] == 0:
                    self.__empty_site_list.append((Location(index_c,index_r)))

    def is_game_over(self):
        return self.__is_empty_loc() and self.__merge_element()
    def __is_empty_loc(self):
        if len(self.__empty_site_list) == 0:
            return True
        return False
    def __merge_element(self):
        for r in range(len(self.__map)-1):
            for c in range(len(self.__map[r])-1):
                if self.__map[r][c] == self.__map[r][c+1] or self.__map[r][c] == self.__map[r+1][c]:
                    return False
        return True



##-----------------------------------------
# test
if __name__ == "__main__":
    gamecorecontroller = GameCoreController()
    gamecorecontroller.move(DirectionModel.RIGHT)
    for item in gamecorecontroller.map:
        print (item)