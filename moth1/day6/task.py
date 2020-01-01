"""


"""
# 1.
bissextile = []
for year in range(1970,2051):
    if (year%4==0 and year%100!=0 or year%400==0):
        bissextile.append(year)
print (bissextile)

# 2.
#[{city:beijing,secnic:[],food:[]},....]

list_china = []
while True:
    city = input("please the city:")
    if(city==""):
        break
    dict_city_food = {"city":city}
    secnics = []
    while True:
        secnic_ = input("Please input the secnic you like:")
        if secnic_ == "":
            break
        secnics.append(secnic_)
    dict_city_food["secnic"] = secnics

    food = []
    while True:
        food_you_like = input("Please input the food you like:")
        if food_you_like == "":
            break
        food.append(food_you_like)
    dict_city_food["food"] = food
    list_china.append(dict_city_food)
#[{city:beijing,secnic:[],food:[]},....]
for dict_city_food in list_china:
    print("the city is %s,the secnic is:"
          %dict_city_food["city"])
    for secnic in dict_city_food["secnic"]:
        print (secnic)
    print ("the food have:")
    for food in dict_city_food["food"]:
        print (food)