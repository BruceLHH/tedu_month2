import random
def ascending_sort(list_):
    """
        sort gived list_ by ascending
        :param list_
        Return: ascended list
    """
    # [2,5,275,7,2,98 ]
    for i in range(len(list_)-1):
        temp = i
        for j in range(i+1,len(list_)):
            if (list_[j]<list_[temp]):
                temp = j
        list_[i],list_[temp] = list_[temp],list_[i]

list_ = [2,5,275,7,2,98,3]
ascending_sort(list_)
print (list_)

coutn_time = 0
def count_time_fun():
    global coutn_time
    coutn_time += 1
def mat_transform(matrix_):
    """

    """
    count_time_fun()
    for row in range(len(matrix_)):
        for col in range(row):
            matrix_[row][col],matrix_[col][row]=matrix_[col][row],matrix_[row][col]

matrix_ = [[1,25,5,2],[3,56,1,8],[3,7,23,1],[9,60,43,27]]
for i in range(random.randint(1,300)):
    mat_transform(matrix_)

print (coutn_time)