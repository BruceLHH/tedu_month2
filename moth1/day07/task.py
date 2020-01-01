#
def print_matrix(list_):
    """
    print list
    :Params list_
    """
    for row in range(len(list_)):
        for col in range(len(list_[row])):
            print (list_[row][col],end=" ")
        print ()

# 2.
def transform(matrix_):
    """
    get the transform of matrix_
    Args: matrix_
    """
    #   [ 2,4,5]
    #   [ 3,6,8]
    #   [ 4,9,2 ]
    for row in range(len(matrix_)):
        for col in range(row):
            matrix_[row][col],matrix_[col][row] = matrix_[col][row],matrix_[row][col]
    print (matrix_)

list_test = [[1,2,5,9],
             [43,7,8,3],
             [76,34,9,1],
             [0,3,76,2]]
print_matrix(list_test)
transform((list_test))
