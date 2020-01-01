import pymysql
import os

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='student_1',
                     charset="utf8"
                     )
cur = db.cursor()
f  = open('mmm.jpg','rb')
data=f.read()

try:
    sql = "insert into class01 values(3,'Iris',%s);"
    cur.execute(sql,[data])
    db.commit()
except Exception as e:
    db.rollback()
    print (e)
f.close()

# sql = "select image from class01 id=1;"
# try:
#     f = open('girl.jpg','wb')
#     cur.execute(sql)
#     data=cur.fetchone()[0]
#     f.write(data)
# except Exception as e:
#     print (e)


cur.close()
db.close()



