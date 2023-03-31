import requests

def lotto_api(num):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=100'
    response = requests.get(url)
    output = response.json()
    return output
class LottoMan:
    def __init__(self):
        self.shop_name = '우리동네 로또가게'
    def answer_lotto_numbers(self, num):
        output = lotto_api(num)
        print("응답")

lot = LottoMan()
output = lot.answer_lotto_numbers(50)