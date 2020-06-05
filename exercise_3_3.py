def print_absolute():
    """절댓값을 알려주는 함수""" #독스트링
    import math
    print('정수를 입력하세요')
    number = int(input())
    abnumber=abs(number)
    print(number,'의 절댓값:',abnumber)
print_absolute()
help(print_absolute)

def print_plus(number1,number2):
    """두 수를 전달받아 그 합계를 화면에 출력하는 함수"""
    print("두 수의 합계:",number1+number2)
print_plus(100,50)

def average_of_4_numbers(num1,num2,num3,num4):
    result=(num1+num2+num3+num4)/4
    print(result)
average_of_4_numbers(512,64,256,192)

def no_return():
    """화면에 메시지를 출력하지만, 값을 반환하지는 않는다."""
    print('이 함수에는 반환값이 없습니다.')

result = no_return()
print(result) #반환값이 없기떄문에 None으로 출력된다.

def area_of_triangle(length,height):
    """밑변과 높이를 입력하면 삼각형 넓이를 출력해준다."""
    area=length*height/2
    return area
result=area_of_triangle(10,8)
print(result)

