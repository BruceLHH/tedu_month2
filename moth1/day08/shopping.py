dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

list_order = []


def gou_wu():
    """
        购物
    :return:
    """
    #
    while True:
        choice = input("1键购买，2键结算。")
        if choice == "1":
            choice_commodity()
        elif choice == "2":
            buy_commodity()


def buy_commodity():
    """

    """
    # print the purchase commodity infomation
    print_purchase_commodity_info()
    #compute the total cost
    cost_all = compute_total_cost()
    while True:
        money = float(input("总价%d元，请输入金额：" % cost_all))
        if money >= cost_all:
            print("购买成功，找回：%d元。" % (money - cost_all))
            list_order.clear()
            break
        else:
            print("金额不足.")


def compute_total_cost():
    cost_all = 0
    for choice in list_order:
        commodity = dict_commodity_info[choice["cid"]]
        cost_all += commodity["price"] * choice["count"]
    return cost_all


def print_purchase_commodity_info():
    for choice in list_order:
        commodity = dict_commodity_info[choice["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], choice["count"]))


def choice_commodity():
    """

    """
    display_commodity_info()
    while True:
        cid = int(input("请输入商品编号："))
        if cid in dict_commodity_info:
            break
        else:
            print("该商品不存在")
    count = int(input("请输入购买数量："))
    list_order.append({"cid": cid, "count": count})
    print("添加到购物车。")


def display_commodity_info():
    for number, value in dict_commodity_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (number, value["name"], value["price"]))


gou_wu()
