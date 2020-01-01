import re

s = """Hello
beijing.
"""

regex = re.compile(r"[a-z]+",flags = re.I)
l = regex.findall(s)
print (l)


regex1 = re.compile(r".+",flags = re.S)
l1 = regex1.findall(s)
print (l1)