

list_person = []
while True:
    person = input("please the figure you like.")
    if person=="":
        for item in list_person:
            print (item)
        max_score = max(list_person)
        min_score = min(list_person)
        mean_score = sum(list_person)/len(list_person)
        print ("the max score: %f,the min score: %f, "
               "the mean of score: %.4f"%(max_score,min_score,
                                          mean_score))
        break
    person = float(person)
    list_person.append(person)