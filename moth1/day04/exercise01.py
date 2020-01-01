# paper_thickness = 0.01
# count = 0
# print (8844.43e+3)
# while paper_thickness<8844.43e+3:
#     paper_thickness *= 2
#     count += 1
# print (count)

import random
random_number = random.randint(1,100)
print(random_number)
while True:
    input_number = int(input("please guess the number:"))
    if input_number<1 or input_number>100:
        print ("please input the number of 1<number<100.")
        continue
    if input_number>random_number:
        print ("big!")
    elif input_number<random_number:
        print("little!")
    else:
        print ("right!",input_number)
        break