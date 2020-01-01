"""
 input students info
"""

# dict_student_info = {}
# while True:
#     name = input("please input name:")
#     if name == "":
#         break
#     age = int(input('please input the age:'))
#     score = int(input("please input the score:"))
#     sex = input("Please input the sex:")
#     value = {"age":age,"score":score,"sex":sex}
#     dict_student_info[name] = value
# #dict{ name:{score: ,age: ,
# for key,value in dict_student_info.items():

dict_student_info = []
while True:
    name = input("please input name:")
    if name == "":
        break
    age = int(input('please input the age:'))
    score = int(input("please input the score:"))
    sex = input("Please input the sex:")
    info  = {"name":name,"age": age, "score": score, "sex": sex}
    dict_student_info.append(info)
# [{name: score: ,age: ,}]
for dict_info in dict_student_info:
    print(dict_info['name'],dict_info["age"])