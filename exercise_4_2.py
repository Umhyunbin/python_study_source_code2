A_birth=0x7d0
A_age=0x12
B_age=0o22
C_age=18
print(A_birth,',',A_age,',',B_age,',',C_age)

print(-2.5287e2)

def almost_equal():
    """두 실수가 거의 같은지 검사하는 함수"""
    import math
    real1=float(input())
    real2=float(input())
    metric=abs(real1-real2)
    return metric
bound=float(input())
result=almost_equal()<bound
print(result)

