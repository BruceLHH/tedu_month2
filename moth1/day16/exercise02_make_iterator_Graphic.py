

class Graphic:
    pass
class GraphManager:
    def __init__(self):
        self.__list_graphic = []
    def add_graphic(self,graphic):
        self.__list_graphic.append(graphic)
    def __iter__(self):
        return GraphIterator(self.__list_graphic)
class GraphIterator:
    def __init__(self,list_graph):
        self.list_graph = list_graph
        self.index = 0
    def __next__(self):
        if self.index >len(self.list_graph)-1:
            raise StopIteration
        item = self.list_graph[self.index]
        self.index += 1
        return item

manager = GraphManager()
manager.add_graphic((Graphic()))
manager.add_graphic((Graphic()))
manager.add_graphic((Graphic()))
manager.add_graphic((Graphic()))

#duotai
ite = manager.__iter__()
while True:
    try:
        item = ite.__next__()
        print (item)
    except StopIteration:
        break

for item in manager:
    print (item)