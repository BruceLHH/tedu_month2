input_number = int(input("input:"))
for item in range(2,input_number):
    if(input_number%item==0):
        print("no")
        break

else:
    print ('yes')