
"""
1. 메뉴수집
2. 메뉴를 관리하는 파일(이름, 가격, 개수)
3. 주문(메뉴 선택, 수량 선택)
4. 확인
"""

menu = {
    '아메리카노':3000,
    '라떼':3500, 
    '카페모카':3500, 
    '자바칩':5000, 
    '딸기라떼':4500, 
    }

def OrderCoffee():

    order = {} # 메뉴이름, 수량
    quantity = {}
    total_price = {}
    while True:
        menu_list = list(menu.keys())
        ShowMenu()
        choice = input("메뉴이름을 입력하시오.\n(주문완료 : q, 메뉴추가 : menu)\n")
        if choice == 'q':
            break
        elif choice == 'menu':
            menu_add()
            continue
        # 입력값이 메뉴에 있으면 수량 입력. 아니면 다시 메뉴 이름 입력
        elif choice in menu_list:
            add_option,add_price = Ice_or_Hot()
            choice2 = add_option + choice
            quantity[choice2] = int(input("수량을 입력하시오\n"))
            total_price[choice2] = (menu[choice]+add_price) * quantity[choice2]
            continue
        elif choice not in menu_list:
            print("다시 입력해주세요")
            continue
    return total_price,quantity

def Ice_or_Hot():
    print("*****옵션을 선택하세요*****")
    print("1. Ice(+500)\n2. Hot")
    s = input()   
    if s == '1':
        v = 500
        temp = 'ICE'
    elif s == '2':
        v = 0
        temp = 'HOT'

    return temp,v

def menu_add():
    key = input('메뉴 입력 : ')
    val = int(input('가격 입력 : '))
    menu[key] = val
    
def Takeout():
    a = input("1. 먹고가기\n2. 포장하기\n")
    if a == '1':
        s = '매장'
    else:
        s = '포장'
    return s

def bill(total_price,quantity,t):
    price = list(total_price.values())
    name = list(total_price.keys())
    cnt = list(quantity.values())
    print("#########################")
    print("####### 주문 내용 #######")
    print("#########################\n")
    print("주문 형태 : %s\n"%t)
    for j in range(len(total_price)):
        print(f"{name[j]}\n가격: {price[j]}, 수량 : {cnt[j]}""\n")

    print("전체금액 : ",sum(price),"원\n")

    return price

def ShowMenu():
    menuLength = len(menu)
    menulist = list(menu.keys())
    menuvalue = list(menu.values())
    print("------------------------")
    print("-----------메뉴----------")
    for i in range(menuLength):
        print("%-10s"%menulist[i],"%s"%menuvalue[i])
    print("------------------------")
    print("------------------------")

#  주문받기
print("스타벅스 키오스크 오신것을 환영합니다.")

# 메뉴 보여주기, 주문 하기
total_price,quantity = OrderCoffee()

# 포장/매장
t = Takeout()

# 주문내역 확인, 총액 확인
price = bill(total_price, quantity,t)

# 결제수단
print("************************")
b = input("\n*결제수단을 고르세요*\n1. 카드, 2. 현금, 3. 포인트\n")
c = int(b)
if c >= 3:
    print(f"포인트로 {sum(price)}원을 결제합니다.")
elif c >= 2:
    print(f"현금으로 {sum(price)}원을 결제합니다.\n현금을 넣어주세요")
else:
    print(f"카드로 {sum(price)}원을 결제합니다.\n카드를 넣어주세요")