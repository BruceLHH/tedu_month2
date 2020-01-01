
class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
class LinkList:
    def __init__(self):
        self.head = Node(None)
    def init__list(self,list_):
        p = self.head
        for item in list_:
            next = Node(item)
            p.next = next
            p = p.next

    def show(self):
        node = self.head.next
        while node:
            print(node.val)
            node = node.next
    def is_empty(self):
        return False if self.head.next else True

    def head_insert(self,val):
        p_node = Node(val)
        p_node.next = self.head.next
        self.head.next = p_node
    def insert(self,index,val):
        p = self.head
        number = 0
        while number != index and p.next:
            p = p.next
            number += 1
        insert_node = Node(val)
        insert_node.next = p.next
        p.next = insert_node
    def delete(self,value):
        p = self.head
        while p.next and p.next.val != value:
            p = p.next
        if p.next is None:
            raise ValueError("error.")
        else:
            p.next = p.next.next
    def get_index(self,index):
        if index<0:
            raise ValueError("index less than 0.")
        p = self.head.next
        for i in range(index):
            p = p.next
            if not p:
                return -1
        return p.val
    def merge_list(self,linklist1,linklist2):
        p = linklist1.head
        q = linklist2.head.next


if __name__ == "__main__":
    list_ = [3,2,{6},{"ss":3},(3,5)]
    llist = LinkList()
    llist.init__list(list_)

    print (llist.is_empty())
    print (llist.get_index(13))
    llist.show()