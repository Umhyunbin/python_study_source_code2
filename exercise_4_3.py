string='I think, therefore I am.'
print(string.replace('think','eat'))

order_memo = """주문1: 아메리카노
주문2: 카페 라테
주문3: 아메리카노, 아메리카노
주문4: 아메리카노, 카페 라테
주문5: 카페 라테, 카페 라테
"""

ord=order_memo.count('주문')
americano=order_memo.count('아메리카노')
print('주문 횟수:',ord,'아메리카노 개수:',americano)
