import os,re
import pymysql


def insert_database(data):
    word = re.findall(r"(\S+)\s*(.*)",data)
    return (word[0][0],word[0][1])


db  = pymysql.connect(host = 'localhost',
                     port= 3306,
                     user = 'root',
                     password='123456',
                     database='dict',
                     charset="utf8")
cur = db.cursor()
sql = "insert into words (word,mean) values(%s,%s);"

f = open('dict.txt','r')
for line in f:
    word,explian = insert_database(line)
    try:
        cur.execute(sql,[word,explian])
        db.commit()
    except Exception as e:
        db.rollback()
        print (e)

cur.close()
db.close()
f.close()
