str1 = input("please input a string:")
for item in str1:
    code_value = ord(item)
    print (code_value)

while True:
    input_str = input("please a value:")
    if not input_str:
        break
    input_value = int(input_str)
    print (chr(input_value))