tuple_01 = ("ww","ee","rr")
iterator = tuple_01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print (item)
    except StopIteration:
        break

dict_01 = {"wq":101,"er":102,"ry":103}
ite = dict_01.__iter__()

while True:
    try:
        item = ite.__next__()
        print (item,dict_01[item])
    except StopIteration:
        break