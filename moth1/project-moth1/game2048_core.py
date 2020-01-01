"""
    2048 game core tec
"""
#
# __list_merge = [[3,0,5,0,3,0],
#               [3,5,5,0,3,0],
#               [3,0,5,4,3,0],
#               [2,0,6,7,3,0]]
# 1. move 0 to tail
# [3,0,3,0] --> [3,3,0,0]

def move_zero_to_tail(list_merge):
    """
    move zero to the tail of list
    Args: __list_merge
    """
    # [ 3,0,3,0,3]
    # print (__list_merge)
    for index in range(-1,-len(list_merge)-1,-1):
        if list_merge[index] == 0:
            del list_merge[index]
            list_merge.append(0)
# 2.
def merge_common_number(list_merge):
    """

    """
    # [3,3,3,0] --> [6, ,3,0]
    move_zero_to_tail(list_merge)
    for index in range(len(list_merge)-1):
        if list_merge[index] == list_merge[index+1]:
            list_merge[index] += list_merge[index+1]
            del list_merge[index+1]
            list_merge.append(0)

#3.
map = [[3, 0, 5, 0, 3, 0],
                 [3, 5, 5, 0, 3, 0],
                 [3, 0, 5, 4, 3, 0],
                 [2, 0, 6, 7, 3, 0],
                [4, 7, 5, 4, 0, 0],
                 [0, 1, 3, 0, 7, 0],
       ]
for line in map:
    print (line)
print ()
def move_left_map(map):
    """

    """
    for line in map:
        merge_common_number(line)
#move_left_map(map)
# print (map)

#4.
def move_right_map(map):
    """

    """
    for line in map:
        line.reverse()
        merge_common_number(line)
        line.reverse()
# move_right_map(map)
# print (map)

# 5.
def map_transform(map):
    """
    transform
    """
    for row in range(len(map)):
        for col in range(row):
            map[row][col],map[col][row] = map[col][row],map[row][col]
def move_up_map(map):
    """

    """
    map_transform(map)
    move_left_map(map)
    map_transform(map)

# move_up_map(map)
def move_down_map(map):
    """

    """
    map_transform(map)
    move_right_map(map)
    map_transform(map)
move_down_map(map)
for line in map:
    print (line)