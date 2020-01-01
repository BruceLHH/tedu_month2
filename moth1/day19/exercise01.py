"""

"""
def verify_permissions(func):
    def wrapper(*args,**kwargs):
        print ("verify acount:")
        func(*args,**kwargs)
    return wrapper

#@verify_permissions
def deposit(money):
    print ("deposit %d money."%money)
@verify_permissions
def withdraw(login_id,pwd):
    print ("withdraw:",login_id,pwd)

deposit(1000)
print()
withdraw("ww",123)

