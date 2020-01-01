"""
get 2D vector's position,direct,number
"""

list01 = [["00","01","02","03"],
["10","11","12","13"],
["20","21","22","23"],
["30","31","32","33"]]

class Vector2:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    @staticmethod
    def left():
        return Vector2(0,-1)
    @staticmethod
    def right():
        return Vector2(0,1)
    @staticmethod
    def up():
        return Vector2(-1,0)
    @staticmethod
    def down():
        return Vector2(1,0)

    # list02, 2,0 , right, 3
    @staticmethod
    def get_element(target,vec_pos,vec_dir,count):
        res = []
        for i in range(count):
            vec_pos.x += vec_dir.x
            vec_pos.y += vec_dir.y
            elem = list01[vec_pos.x][vec_pos.y]
            res.append(elem)
        return res
# print(Vector2.get_element(list01,Vector2(0,1),Vector2.down(),3))