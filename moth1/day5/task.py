#1 .

# list_str = []
# while True:
#     temp = input("please input a string")
#     if temp!= "":
#         list_str.append(temp)
#     else:
#         res = "".join(list_str)
#         print("the result is: ",res)
#         break

# 2.
str = "how are you"
list_str = str.split(" ")
res = list_str[::-1]
print (" ".join(res))

# 3.
list01 = [43,6,2,7,3,65,9]
min_number = list01[0]
for item in list01:
    if(min_number>item):
        min_number = item
print (min_number)

# 4.

import random
lottery = []
while len(lottery) < 6:
    temp = random.randint(1,33)
    if temp not in lottery:
        lottery.append(temp)
lottery.append(random.randint(1,16))
print ("lottery is:", lottery)

buy_lottery = []
index = 1
while( len(buy_lottery)< 6):
    buy = int(input("please choice the %d red boll:"%index))
    if(buy<1 or buy>33):
        print ("you choice's boll number is more than the scope.")
        continue
    if buy in buy_lottery:
        print ("the boll is repetition")
        continue
    buy_lottery.append(buy)
    index += 1
buy_lottery.append(int(input("please choice the blue boll.")))
print ("you purchased a lottory successful:",buy_lottery)
