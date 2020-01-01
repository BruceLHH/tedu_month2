"""


"""
#1.
string = "  x x: z qgix,hdzw.   "
print (string.count('w',0,len(string)))
print (string.index("zw"))
print (string.lstrip())
print (string.rstrip())
print (string.startswith("x x"))
string.replace()
# 1.
def fun07(a=8,b=0,*args,c,d,**Kargs):
    print (a,"\n",b,"\n",args,"\n",c,"\n",d,"\n",Kargs)

# fun07("lin","j,e,y,s",c=56,d="jipl",f=54,e=23)
a = (10000,)
b = (10000,)
print (id(a),id(b))
print (a is b,"\n",a==b)

susu = []

def is_prime(item):
    """"""
    return is_susu(item)


def is_susu(item):
    if item < 2:
        return False
    for i in range(2, item):
        if (item % i == 0):
            return False
    else:
        return True


def judge_susu(a,b):
    """"""
    if(b<0):
        return -1
    return [item for item in range(a,b+1) if is_prime(item)]
judge_susu(-5,-1)
print ()