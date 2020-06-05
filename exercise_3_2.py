import math

print('수를 입력해 주세요')
number = int(input())

result = round(math.sqrt(number * math.pi))
print('계산 결과:', result)

#호출되는 함수 이름 : print,int,round,math.sqrt,input