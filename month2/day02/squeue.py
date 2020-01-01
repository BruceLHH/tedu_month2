"""

"""
class SqueueError(Exception):
    pass
class SQueue:
    def __init__(self):
        self.__squeue = []
    # def __str__(self):
    #     return self.__squeue
    def is_empty(self):
        """
        judge squeue is or not empty
        :return bool
        """
        return not len(self.__squeue)
    def esqueue(self,val):
        self.__squeue.append(val)
    def dequeue(self):
        if not self.__squeue:
            raise SqueueError("empty.")
        return self.__squeue.pop(0)

if __name__ == "__main__":
    sq01 = SQueue()
    print(sq01.is_empty())
    sq01.esqueue(3)
    sq01.esqueue(9)
    sq01.esqueue(2)
    sq01.esqueue(5)
    print (sq01.dequeue())