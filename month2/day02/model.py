class MatchStr:
    def __init__(self,right):
        self.left = ""
        self.right = right
        self.__get_left_str()
    def __get_left_str(self):
        """
        get right string according left string.
        """
        if self.right == "{":
            self.left = "}"
        if self.right == "(":
            self.left = ")"
        if self.right == "[":
            self.left = "]"