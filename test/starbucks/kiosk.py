class Menu:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category

class Order:
    def __init__(self,OrderName,quantity):
        self.OrderName = OrderName
        self.quantity = quantity
    def ChangeMenu(self,new_name,new_quantity):
        self.OrderName = new_name
        self.quantity = new_quantity

menulist = []
americano = Menu("아메리카노",4000,"음료")
menulist.append(americano)
latte = Menu("라떼",4000,"음료")
menulist.append(latte)
mocha = Menu("카페모카",4500,"음료")
menulist.append(mocha)
cake = Menu("케익",6000,"베이커리")
menulist.append(cake)
bagle = Menu("베이글",5500,"베이커리")
menulist.append(bagle)

def Menu_add():
    menu, price,category = input("메뉴,가격,카테고리 입력").split()
    price = int(price)
    

# 메뉴 리스트 출력
for i in range(len(menulist)):
    print(f"{menulist[i].name} +{menulist[i].price}")
