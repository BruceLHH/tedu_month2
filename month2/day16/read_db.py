import pymysql
db = pymysql.connect(host = 'localhost',
                     port= 3306,
                     user = 'root',
                     password='123456',
                     database='student',
                     charset="utf8")
##get cursor
cur = db.cursor()

sql = "select * from class01 where sex='u';"
cur.execute(sql)

#get one res
one_row = cur.fetchone()
print (one_row)

# get many res
many_row = cur.fetchmany(3)

cur.close()
db.close()

