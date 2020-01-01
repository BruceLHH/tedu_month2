lisxt01 = [4,5,7,3,9,10]
# 1.
# for item in lisxt01:
#     if(item %2 ==0):
#         print (item)

# 2. yield
def get_nev(lisxt01):
    index = 0
    while index<len(lisxt01):
        if (lisxt01[index]%2==0):
            yield lisxt01[index]
        index +=1
for item in get_nev((lisxt01)):
    print (item)