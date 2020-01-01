
#match
import re
pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)
obj = regex.search("abcdefghi")

print (obj.pos)
print (obj.endpos)
print (obj.re)
print( obj.string)
print (obj.lastgroup)
print (obj.lastindex)
print ()
print(obj.span())
print (obj.start())
print (obj.end())
print (obj.groupdict())
print (obj.groups())