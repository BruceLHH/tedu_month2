
def compute(hour=0,mins=0,s=0):
    hour_res = hour*60*60
    min_res = mins*60
    return hour_res+min_res+s

res = compute(mins =54,s=65)
print (res)

