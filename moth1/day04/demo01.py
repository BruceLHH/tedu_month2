
import random
random_number = random.randint(1,100)
print(random_number)
count = 0;
while count<3:
    count +=1
    input_number = int(input("please guess the number:"))
    if input_number<1 or input_number>100:
        print ("please input the number of 1<number<100.")
        continue
    if input_number>random_number:
        print ("big!")
    elif input_number<random_number:
        print("little!")
    else:
        print ("right!",count)
        break
else:
    print('fail,game over!')

