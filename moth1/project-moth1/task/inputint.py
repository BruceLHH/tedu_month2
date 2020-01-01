
class InputInt():
    """
    judge input, and modify to right.
    """
    def rightwrite(self,str):
        """
        repeat input vlaue to right.
        :return: self.value
        """
        while True:
            try:
                self.value = int(input("Please input the %s: "%str))
            except Exception:
                print ("please input a number.")
                continue
            break
        return self.value