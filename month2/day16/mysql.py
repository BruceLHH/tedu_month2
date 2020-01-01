import pymysql
db = pymysql.connect(host = 'localhost',
                     port= 3306,
                     user = 'root',
                     password='123456',
                     database='student',
                     charset="utf8")
##get cursor
cur = db.cursor()

# 1. write
# sql1 = "insert into class01 values(5,'Aimy',14,'w',99,'2018-10-16');"
# sql = "insert into class01 values(3,'huangshang',45,'m',86,'2016-1-22');"
# cur.execute(sql1)
# db.commit()

try:
    # id = input("id:")
    # name=input("name:")
    # age=input("age:")
    # score=input("score:")
    ## 1.1
    #sql = "insert into class01 (id,name,age,score) values(%d,'%s',%d,%d);"%(int(id),name,int(age),int(score))
    #cur.execute(sql)
    ## 1.2
    # sql = "insert into class01 (id,name,age,score) values(%s,%s,%s,%s);"
    # cur.execute(sql,[id,name,age,score])

    ## 2.
    #sql = "update class01 set sex='w' where name='iiii'"
    sql = "delete from class01 where score<40"
    cur.execute(sql)
    db.commit()
except Exception as e:
    db.rollback()
    print(e)



# 2. read
# sql = "select name,score from class01 where sex='m';"
# cur.execute(sql)
# one_row = cur.fetchone()
# print(one_row)
# two_row = cur.fetchmany(3)
# print (two_row)

cur.close()
db.close()

