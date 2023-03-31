# 마지막 줄이 왜 1번 선택했을때만 출력되는지 모르겠다.
# 2번에서는 출력이 안됨

class Menu:
    def __init__(self,num,name,price):
        self.name = name
        self.price = price
        self.num = num
    def __str__(self):
        return f"{self.name}: {self.price}원"
    def add_menu(self,name,price):
        if name:
            self.name = name
        if price:
            self.price = price
        
class Order():
    def __init__(self,menu,quantity,temperature):
        self.menu = menu
        self.quantity = quantity
        self.total_price = (menu.price +temperature) * quantity
        
    def __str__(self):
        return f"{self.menu.name} 수량: {self.quantity} 총: {self.total_price}원"
    def update_order(self,quantity):
        if quantity:
            self.quantity = quantity
            self.total_price = self.menu.price * self.quantity

drink_items = [
    Menu(1,"아메리카노",4000),
    Menu(2,"라떼",4000),
    Menu(3,"카페모카",4500),
    Menu(4,"딸기라떼",6000),
    Menu(5,"푸라푸치노",7000)
]

bakery_items = [
    Menu(1,"딸기케익",8000),
    Menu(2,"생크림케익",9000),
    Menu(3,"프레즐",5000),
    Menu(4,"마카롱",2000),
    Menu(5,"베이글",5500)
]

Dorder_list = []
Border_list = []
total = 0
while True:
# 메뉴 리스트 출력
    print("*"*30)
    print("주문을 입력하세요")
    print("*"*30)
    print("1. 음료 주문")
    print("2. 베이커리 주문")
    print("3. 수량 수정")
    print("4. 총 주문금액")
    print("5. 주문 종료")

    choice = input()
    if choice == "1":
        print("카페 메뉴")
        print("*"*30)
        for i,item in enumerate(drink_items):
            print(f"{item.num}.{item.name}:{item.price}")
        menu_choice= int(input("주문할 메뉴 번호를 입력하세요: "))
        order_menu = drink_items[menu_choice-1]
        menu_temp = int(input("1. ICE(+500) 2. HOT :"))
        if menu_temp == 1:
            t = 500
        elif menu_temp == 2:
            t = 0
        else:
            print("잘못 입력하셨습니다. 다시 입력하세요.")
            continue
        menu_quantity = int(input("수량을 입력하세요.:"))
        order= Order(order_menu,menu_quantity,t)
        Dorder_list.append(order)
        print(f"{order_menu.name}이(가){menu_quantity}개 주문되었습니다.")
    if choice == "2":
        for i,item in enumerate(bakery_items):
            print(f"{i+1}.{item.name}:{item.price}")
        menu_choice= int(input("주문할 메뉴 번호를 입력하세요: "))
        order_menu = bakery_items[menu_choice-1]
        menu_quantity = int(input("수량을 입력하세요. :"))
        t = 0
        order= Order(order_menu,menu_quantity,t)
        Border_list.append(order)
        print(f"{order_menu.name}이(가){menu_quantity}개 주문되었습니다.")
    elif choice == "3":
        category_choice = input("1. 음료수정 2. 베이커리 수정")
        if category_choice == '1':
            print("*****음료 주문*****")
            for i,order in enumerate(Dorder_list):
                print(i+1,order)
            menu_choice = int(input("수정할 메뉴 번호를 입력하세요 : "))
            new_quantity = int(input("수정할 수량을 입력하시오. :"))
            Dorder_list[menu_choice-1].update_order(new_quantity)
            print(f"{Dorder_list[menu_choice-1].menu.name}의 수량이 수정되었습니다.")
        if category_choice =='2':
            print("*****베이커리 주문*****")
            for i,order in enumerate(Border_list):
                print(i+1,order)
            menu_choice = int(input("수정할 메뉴 번호를 입력하세요 : "))
            new_quantity = int(input("수정할 수량을 입력하시오. : "))
            Border_list[menu_choice-1].update_order(new_quantity)
            print(f"{Dorder_list[menu_choice-1].menu.name}의 수량이 수정되었습니다.")
    elif choice == "4":
        print("*****음료 주문*****")
        for order in Dorder_list:
            print(order)
            total += order.total_price
        print("*****베이커리 주문*****")
        for order in Border_list:
            print(order)
            total += order.total_price
        print(f"총 주문 금액: {total}원")
    
    elif choice == "5":
        print("프로그램을 종료합니다.")
        break
    
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")
