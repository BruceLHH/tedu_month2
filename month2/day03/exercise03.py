
def get_mul(vlaue):
    if vlaue<= 1:
        return vlaue
    return vlaue * get_mul(vlaue-1)
print(get_mul(6))

