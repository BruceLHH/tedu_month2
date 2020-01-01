"""
    input : month
    output: season or error
"""
# month = int(input("input:"))
# if (month>12 or month <1):
#     print("input is error!")
# elif(month>9):
#     print ("The four season.")
# elif(month>6):
#     print("The three season.")
# elif (month > 3):
#     print("The two season.")
# else:
#     print ("the one season")

# age = int(input("input:"))
# if (age>150 or age <0):
#     print("input is error!")
# elif(age>65):
#     print ("old man.")
# elif(age>20):
#     print("chenglian.")
# elif (age > 13):
#     print("yong.")
# elif (age > 2):
#     print("children.")
# else:
#     print ("baby")

hight = float(input("input hight:"))
weight = float(input("input weight"))
BMI = weight/(hight**2)
if(BMI<0):
    print("input is error!")
elif(BMI<18.5):
    print("BMI is lower")
elif(BMI<24):
    print("BMI is normal")
elif(BMI<28):
    print("BMI is too weight")
elif(BMI<30):
    print("BMI is fat 1")
elif(BMI<40):
    print("BMI is fat 2")
else:
    print("fat 3")