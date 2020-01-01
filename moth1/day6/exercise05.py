"""
  get user interest
"""

interest = []
while True:
    user = input("please you name:")
    if not user:
        break
    interest_person = [user,]
    count = 1
    while True:
        inte = input("please input your %dth interest:"%count)
        if inte == "":
            break
        interest_person.append(inte)
        count += 1
    interest.append(interest_person)
#[[name,...],[]...]
print (interest)
for user_inte in interest:
    print ("%s's interest have:"%user_inte[0])
    for inte_index in range(1,len(user_inte)):
        print (user_inte[inte_index])
