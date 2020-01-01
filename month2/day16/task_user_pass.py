import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='user',
                     charset='utf8')
cur = db.cursor()

## register.
def register():
    name = input("input register name:")
    sql = "select name from user where name=%s;"
    cur.execute(sql,[name])
    is_exist = cur.fetchone()
    if is_exist:
        return False
    sql01 = "insert into user values(%s,%s)"
    password = input("input your password:")
    cur.execute(sql01,[name,password])
    db.commit()
    return True

## sign in
def sign_in():
    name = input("input sign in name:")
    passwd = input("input sign in password:")
    sql = "select * from user where name=%s and passwd=%s;"
    cur.execute(sql,[name,passwd])
    info = cur.fetchone()
    if info:
        return True
    return False

while True:
    print ("""
    ----------------------
    1.register   2.sign in 
    ----------------------
    """)
    num = input ("input selection.")
    if num == '1':
        if register():
            print ("register success.")
        else:
            print("The user is exist,please repeat input:")
    elif num == '2':
        if sign_in():
            print ("logn in success. ")
            break
    else:
        print ("please repeat input.")

cur.close()
db.close()

