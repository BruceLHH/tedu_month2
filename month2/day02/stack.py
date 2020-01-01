from day02.model import MatchStr
class Stack:
    def __init__(self):
        self.__stack = []

    def is_empty(self):
        return not len(self.__stack)
    def push_stack(self,val):
        self.__stack.append(val)
    def pop(self):
        if len(self.__stack)==0:
            raise ValueError("stack is empty.")
        return self.__stack.pop()
    # def nibonan(self,val):
    #     if type(val)==int:
    #         self.push_stack(val)
    #     else:
    #         value1= self.pop()
    #         value2= self.pop()
    #         #self.push_stack(value2"val"value1)

    # task
    def is_str_match(self,str):
        for item in str:
            if item not in ("{","(","[","}",")","]"):
                continue
            if item == "{" or item == "(" or item == "[":
                self.push_stack(item)
                continue
            if self.__not_match_str(item):
                return False
        if self.is_empty():
            return True
        return False


    def __not_match_str(self,item):
        item_obj = MatchStr(item)
        if self.is_empty() or self.pop() != self.__get_match_str(item_obj):
            return True
        else:
            self.pop()
            return False
    # inherit
    def __get_match_str(self,str):
        return str.right

if __name__ == "__main__":
    testobj = Stack()
    list01 = list("jkslaie(lkdjs){fdjsia[flkds]if}")
    str = "jkslaie(lkdjs){fdjsia[flkds]if}"
    str01 = "{}()"
    print (testobj.is_str_match(str01))
