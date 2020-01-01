import time
print (time.time())

print (time.localtime())

# 7 1 2 3 4 5 6
# 2013/3/5
tuple_week = ("w","t","w","s","f","staday","sunday")
def Print_week(riqi):
    tuple_time = time.strptime(riqi,"%y/%m/%d")
    print (tuple_time[6])

Print_week("19/12/17")

"""
birthday -> time_tuple ->time_chou

"""
def caculate_days(birthday):
    """

    :param birthday:
    :return:
    """
    birthday_time_tuple = time.strptime(birthday,"%y/%m/%d")
    birthday_time_chou = time.mktime(birthday_time_tuple)
    print((time.time() - birthday_time_chou)/(24*3600))
caculate_days("87/8/24")