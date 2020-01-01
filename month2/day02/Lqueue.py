class Node:
    def __init__(self,val,next = None):
        """
        creat a Node
        """
        self.val = val
        self.next = next
class LQueueError(Exception):
    pass

class LQueue:
    def __init__(self):
        self.__front = self.__rear = Node(None)
    def is_empty(self):
        return self.__rear == self.__front
    def enqueue(self,val):
        self.__rear.next = Node(val)
        self.__rear = self.__rear.next
    def dequeue(self):
        if self.is_empty():
            raise LQueueError("empty")
        self.__front = self.__front.next
        return self.__front.val

if __name__ == "__main__":
    ls = LQueue()
    ls.enqueue(3)
    ls.enqueue(7)
    ls.enqueue(9)
    ls.enqueue(1)
    ls.enqueue(37)
    while not ls.is_empty():
        print (ls.dequeue())