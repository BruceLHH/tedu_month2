set01 = set()
while True:
    str = input("Please a string")
    if str == "":
        break
    set01.add(str)
print (set01)

manager = set(['caocao',"liube","shunqua"])
tec = set(["caocao","liube","zhangfei","guanyu"])
answer1 = manager&tec
answer2 = tec-manager
answer3 = manager-tec
answer4 = set(["zhangfei"])<manager
answer5 = answer2&answer3
answer6 = manager|tec
print (answer1)
print (answer2)
print (answer3)
print (answer4)
print (answer5)
print (answer6)

