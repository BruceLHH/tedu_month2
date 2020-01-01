

list_person = []
while True:
    person = input("please the figure you like.")
    if person=="":
        for index in range(len(list_person)-1,-1,-1):
            print (list_person[index])
        break
    #person = float(person)
    if person in list_person:
        print("the person is exist!")
    else:
        list_person.append(person)