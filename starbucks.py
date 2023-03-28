
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
    '자바칩푸라푸치노':5000, 
    '딸기라떼':4500, 

    }

order = {} # 메뉴이름, 수량

# 주문받기
# print(list(menu.keys())[0])
menu_list = list(menu.keys())
print("스타벅스 키오스크 오신것을 환영합니다.")
for i in range(len(menu)):
    num = input('%s는 몇잔 주문하시겠어요?'%menu_list[i])
    order[menu_list[i]] = int(num)


# 계산
# 메뉴에서 키를 가져옴
# 가격도 가져옴
# order 에서는 수량을 가져옴
# 계산 -> 마무리
# price = menu[menu_list]
# amount = order[menu_list]
# total = price * amount

price = []
amount = []
total = []

for k in range(len(menu)):
    price.append(menu[menu_list[k]])
    amount.append(order[menu_list[k]])
    total.append(price[k] * amount[k])

print("#########################")
print("####### 주문 내용 #######")
print("#########################")
for j in range(len(menu)):
    if total[j] == 0:
        continue
    else:
        print(f"{menu_list[j]} 가격: {total[j]}, 수량 : {amount[j]}""\n")
print("전체금액 : ",sum(total),"원")

b = input("\n*결제수단을 고르세요*\n1. 카드, 2. 현금, 3. 포인트\n")
c = int(b)
if c >= 3:
    print(f"포인트로 {sum(total)}원을 결제합니다.")
elif c >= 2:
    print(f"현금으로 {sum(total)}원을 결제합니다.")
else:
    print(f"카드로 {sum(total)}원을 결제합니다.")