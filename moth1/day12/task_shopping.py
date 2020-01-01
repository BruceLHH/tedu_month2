"""

shopping cart
"""
class ShoppingCartModel:
    def __init__(self,name = "",price=0,number=0,id=0):
        self.name = name
        self.price = price
        self.number = number
        self.id = id

class ShoppingCartController:
    init_id = 10000
    def __init__(self):
        self.list_shopping = []
    def add_goods(self):
        name = input("Please input you want to buy itme.")
        price = int(input("Please input price:"))
        number = int(input("Please input number."))
        id = self.__get_id()
        goods = ShoppingCartModel(name,price,number,id)
        self.list_shopping.append(goods)
    def __get_id(self):
        ShoppingCartController.init_id += 1
        return ShoppingCartController.init_id
    def display_goods_info(self):
        for item in self.list_shopping:
            print(item.id,item.name,item.price,item.number)
    def remove_goods(self,id):
        for item in self.list_shopping:
            if id == item.id:
                self.list_shopping.remove(item)
    def modify_goods_info(self):
        name = input("Please input the goods's new name.")
        price = int(input("Please input the new price."))
        number = int(input("input the number."))
        id = int(input("Please input the id you want to modify."))
        for item in self.list_shopping:
            if item.id == id:
                item.name = name
                item.price = price
                item.number = number
                return True
        return False
    def sorting_goods_by_price(self):
        pass

# class Goods:
#     def __init__(self,price,number):
#         self.price = price
#         self.number = number
#     def caculate_all_price(self):
#         return self.price *self.number
# class 

class ShoppingCartView:
    def __init__(self):
        self.__manager = ShoppingCartController()
    def __display_menu(self):
        print ("1) please choice goods infomation.")
        print("2) display goods infomation:")
        print("3) remove goods info:")
        print("4) updata goods info:")
        print("5) sort goods by price:")
    def __choice_menu(self):
        num = int(input("Please input number:"))
        if num == 1:
            self.__add_goods()
        elif num == 2:
            self.__display_goods()
        elif num ==3:
            pass
        elif num ==4:
            pass
        elif num ==5:
            pass
        else:
            pass
    def __add_goods(self):
        self.__manager.add_goods()
    def __display_goods(self):
        self.__manager.display_goods_info()

    def main(self):
        while True:
            self.__display_menu()
            self.__choice_menu()

view = ShoppingCartView()
view.main()