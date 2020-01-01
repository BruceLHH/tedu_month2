import pymysql
import hashlib

### password jiayan
SALT = "*@fh!!_"  ## any string is OK.
class Database:
    def __init__(self,host = 'localhost',
                 port =3306,
                 user='root',
                 password='123456',
                 database=None,
                 charset='utf8'):
        self.__host = host
        self.__port=port
        self.__passwd = password
        self.__user=user
        self.__database=database
        self.__charset = charset
        self.__connect_database()
    def __connect_database(self):
        self.db = pymysql.connect(host= self.__host,
                             port = self.__port,
                             user = self.__user,
                             password = self.__passwd,
                             database=self.__database,
                             charset=self.__charset)
    def close(self):
        self.db.close()
    def create_cursor(self):
        self.cur=self.db.cursor()


    def register(self,name,passwd):
        sql="select * from user where name='%s'"%name
        self.cur.execute(sql)
        r = self.cur.fetchone()

        if r:
            return False

        ## password jia mi.
        passwd = self.passwd_encryption(name, passwd)
        sql = "insert into user (name,password) values(%s,%s);"
        try:
            self.cur.execute(sql,[name,passwd])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    def login(self,name,passwd):
        sql = "select * from user where name='%s'" % name
        self.cur.execute(sql)
        passwd_origin = self.cur.fetchone()[2]
        pass_new = self.passwd_encryption(name,passwd)
        if pass_new == passwd_origin:
            return True
        return False
        #### method 2. first encryption ; second, select *** (name,passwd) **
    def query(self,word):
        sql = "select mean from words where word='%s'"%word
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return r[0]
    def insert_history(self,name,word):
        sql = "insert into history (name,word) values(%s,%s);"
        try:
            self.cur.execute(sql,[name,word])
            self.db.commit()
        except Exception:
            self.db.rollback()
    def get_histroty(self,name):
        sql = "select word from history where name='%s' order by time DESC;"%name
        self.cur.execute(sql)
        before_ten = self.cur.fetchmany(10)
        print ("before_ten:",before_ten)
        if len(before_ten) != 0:
            return before_ten
    def passwd_encryption(self, name, passwd):
        hash = hashlib.md5((name + SALT).encode())
        hash.update(passwd.encode())
        passwd = hash.hexdigest()
        return passwd





