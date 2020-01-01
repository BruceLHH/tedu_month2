import re


s = "Alex:1994,Sunny:1984"
pattern = r"(\w+):(\d+)"

#3 re diaoyong
l = re.findall(pattern,s)
print (l)

regex = re.compile(pattern)
l1 = regex.findall(s,0,14)
print (l1)

## qie ge
l01 = re.split(r'[:,]',s)
print (l01)

l02 = re.sub(r":",'-',s)
print (l02)