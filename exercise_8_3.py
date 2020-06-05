class Coordinate:
    """좌표를 나타내는 클래스"""
    x=0
    y=0


    def distance(self,point_2):
        return math.sqrt(square(self.x - point_2.x) +
                         square(self.y - point_2.y))

point_1=Coordinate()
point_2=Coordinate()

point_1.x=-1
point_1.y=2
point_2.x=2
point_2.y=3

import math

def square(x):
    """전달받은 수의 제곱을 반환한다."""
    return x * x

def distance(point_1, point_2):
    """두 점 사이의 거리를 계산해 반환한다. (피타고라스의 정리)"""
    return math.sqrt(square(point_1.x - point_2.x) +
                     square(point_1.y - point_2.y))

print(distance(point_1,point_2))

print(point_1.distance(point_2))


