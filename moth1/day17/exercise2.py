list01 = [43,5,False,"ll",None,9,2," "]
def get_int_generate():
    for item in list01:
        if type(item)==int:
            yield item
ite = get_int_generate()
for item in ite:
    print (item)

# ite1 = (item for item in list01 if type(item)==int)
# for item in ite1:
#     print (item)
#
# ite2 = [item for item in list01 if type(item)==int]
# for item in ite2:
#     print (item)
