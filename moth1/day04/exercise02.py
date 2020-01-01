count =0
while count<3:
    score_str = input("please input score.")
    if not score_str:
        break
    score = int(score_str)
    if score<0 or score>100:
        print ("input error!")
        count += 1
    elif score>90:
        print("A")
    elif score>80:
        print("B")
    elif(score>60):
        print("C")
    else:
        print("D")
else:
    print("error too more!")