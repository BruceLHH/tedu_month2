class StackError(Exception):
    pass
class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LStack:
    def __init__(self):
        self.__top = None
    def is_empty(self):
        return not self.__top
    def push(self,val):
        self.__top = Node(val,self.__top)
    def pop(self):
        if self.__top == None:
            raise StackError("stack is empty.")
        value = self.__top.val
        self.__top = self.__top.next
        return value
    def top(self):
        if self.is_empty():
            return None
        return self.__top.val

if __name__ == "__main__":
    lstack = LStack()
    lstack.push(3)
    lstack.push(5)
    lstack.push(8)
    lstack.push(1)
    print (lstack.pop())
    print (lstack.is_empty())