import re

s = "this year is 2019,70 zhounian of jianguo."
pattern = r"\d+"

it = re.finditer(pattern,s)
for i in it:
    print (i.group())

m = re.fullmatch(r"[ ,\w]+",s)
print (m)

m1 = re.match(r'\w+',s)
print (m1.group())