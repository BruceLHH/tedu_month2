"""
    judge grade

"""
# score = float(input("please the score:"))
# if(score>=90 and score<=100):
#     print("A")
# elif(score<90 and score >= 80):
#     print("B")
# elif(score<80 and score >= 60):
#     print("C")
# elif(score<60 and score>=0):
#     print ("fail")
# else:
#     print ("the input is error!")

month = int(input("Please input the month:"))
if(month<1 or
        month >12):
    print("the input is error")
else:
    if(month>7):
        if(month%2):
            print ("30 days")
        else:
            print("31 days")
    else:
        if(month==2):
            print ("28 days")
        elif(month % 2):
            print("31 days")
        else:
            print ("30 days")
