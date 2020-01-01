"""
model data
"""
class Location:
    def __init__(self,r,c):
        self.index_r = r
        self.index_c = c


class DirectionModel:
    """
    derection data,
    constant
    """
    UP = 0
    DOWM = 1
    LEFT = 2
    RIGHT =3