class Store():
    def __init__(self,category,storename):
        self.storename = storename
        self.category = category
    def __str__(self):
        return f"안녕하세요 {self.storename}점 입니다." 

class Menu(Store):
    def __init__(self,category,storename,menu : dict):
        self.menu = menu
        super().__init__(storename,category)
    def __str__(self):
        return f"{self.category} {self.storename}점의 {self.menu}"
    def add_menu(self,menu):
       self.menu.update(menu)

class Order(Menu):
    def __init__(self,menu,ordermenu,quantity,orderprice):
        super().__init__(menu)
        self.ordermenu = ordermenu
        self.orderprice = orderprice
        self.quantity = quantity
    def total_price(self,ordermenu):
        self.total_price = self.menu[ordermenu] * self.quantity
        return self.total_price

store_list = [
    Store("베이커리","파리바게트"),
    Store("베이커리","뚜레쥬르"),
    Store("카페","투썸플레이스"),
    Store("카페","이디야"),
    Store("카페","스타벅스"),
    Store("한식","서울식당"),
    Store("분식","엽기떡볶이"),
    Store("분식","신전떡볶이"),
]  
menu_list = [
    Menu("베이커리","파리바게트",{"소금빵":3000}),
    Menu("베이커리","뚜레쥬르",{"소금빵":4000}),
    Menu("카페","투썸플레이스",{"아메리카노":3000,"라떼":4000}),
    Menu("카페","이디야",{"아메리카노":5000,"딸기라뗴":6500,"푸라푸치노":7000}),
    Menu("카페","스타벅스",{"아메리카노":2000,"자허블":7000,"돌체라떼":5500}),
    Menu("한식","서울식당",{"김치찌개":8000,"된장찌개":6000,"생선구이":9000}),
    Menu("분식","엽기떡볶이",{"순한맛":8000,"중간맛":6000,"매운맛":9000}),
    Menu("분식","신전떡볶이",{"빨간떡볶이":7000,"간장떡볶이":6000,"크림떡볶이":10000}),
]
order_list = []
while True:
# 메뉴 리스트 출력
    print("*"*30)
    print("1. 카페")
    print("2. 베이커리")
    print("3. 한식")
    print("4. 중식")
    print("5. 총 가격")
    print("6. 주문 종료")
    choice = input()
    if choice == "1":
        print("카페 메뉴")
        print("*"*30)
        for item in menu_list:
            if item.category == '카페':
                print(f"{item.storename}:{item.menu}")
        menu_choice= input("주문할 메뉴를 입력하세요: ")
        order_menu = menu_list[menu_choice]
        menu_quantity = int(input("수량을 입력하세요."))
        order= Order(order_menu,menu_quantity)
        order_list.append(order)
        print(f"{order_menu.menu.keys()}이(가){menu_quantity}개 주문되었습니다.")
'''  if choice == "2":
        for i,item in enumerate(bakery_items):
            print(f"{i+1}.{item.name}:{item.price}")
        menu_choice= int(input("주문할 메뉴 번호를 입력하세요: "))
        order_menu = bakery_items[menu_choice-1]
        menu_quantity = int(input("수량을 입력하세요."))
        t = 0
        order= Order(order_menu,menu_quantity,t)
        Border_list.append(order)
        print(f"{order_menu.name}이(가){menu_quantity}개 주문되었습니다.")
    elif choice == "3":
        category_choice = input("1. 음료수정 2. 베이커리 수정")
        if category_choice == '1':
            print("*****음료 주문*****")
            for i,order in enumerate(Dorder_list):
                print(order)
            menu_choice = int(input("수정할 메뉴 번호를 입력하세요: "))
            new_quantity = int(input("수정할 수량을 입력하시오."))
            Dorder_list[menu_choice]
            # new_menu = drink_items[menu_choice-1].num
            # Dorder_list[new_menu].update_order(new_quantity)
            # print(f"{Dorder_list[menu_choice-1].name}의 수량이 수정되었습니다.")
        if category_choice =='2':
            print("*****베이커리 주문*****")
            for i,order in enumerate(Border_list):
                print(order)
            menu_choice = int(input("수정할 메뉴 번호를 입력하세요: "))
            new_quantity = int(input("수정할 수량을 입력하시오."))
            # new_menu = bakery_items[menu_choice-1]
            # Border_list[new_menu].update_order(new_quantity)
            # print(f"{Border_list[menu_choice-1].name}의 수량이 수정되었습니다.")
    
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

ny = Menu("카페","투썸플레이스",{"아메리카노":5000})
menuadd = ny.add_menu({'라떼':6000})
print(ny)'''