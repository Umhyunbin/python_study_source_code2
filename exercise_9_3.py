print('첫번째 수를 입력하시오: ', end='')  #질문
number1 = int(input())
print('두번째 수를 입력하시오: ', end='')
number2 = int(input())

add = number1 + number2
subtract = number1 - number2
multiply = number1 * number2
divide = number1 / number2

def divide(number1,number2):  #처음엔 def 안썼는데 안돼서 한 번 써봤다.

    try:
        number1 = int(input())
        number2 = int(input())
        divide = number1 / number2
        print(number1, '/', number2, '=', divide)
    except ZeroDivisionError:
        print('None')

print(number1, '+', number2, '=', add)
print(number1, '-', number2, '=', subtract)
print(number1, '*', number2, '=', multiply)
print(number1, '/', number2, '=', divide)