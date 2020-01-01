dict01 = {}
while True:
    goods = input("please input the goods:")
    if goods == "":
        break
    price = int(input("please input the price:"))
    dict01[goods] = price

for key,value in dict01.items():
    print (key,": ",value)