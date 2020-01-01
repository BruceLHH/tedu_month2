name = 'lin'
age = 53
score=99.8
message = "my name is %s,age is %d, score is %.2f"%(name,age,score)
print (message)

# 2.
# input_number = int(input("please the number"))
# empty_number = (input_number-2)
# print ('*'*input_number)
# for item in range(empty_number):
#     print ("*"+" "*empty_number+"*")
# print ('*'*input_number)

# 3.
# input_str = input("plese s string:")
# minddle_index = len(input_str)//2
# reverse_str = input_str[::-1]
# print (input_str[:minddle_index],'\n',reverse_str)
# if (input_str[:minddle_index] == \
#     reverse_str[:minddle_index]):
#     print ("yes")
# else:
#     print ("no!")

# 4.?????
hight = 100
all_distance = hight
count = 0
while hight>=0.01:
    hight = hight / 2
    all_distance += hight * 2
    count += 1
print ("the all dis is:",all_distance,
       "the count is:",count)

# 5.