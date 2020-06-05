import math


class Coordinate:
    """좌표를 나타내는 클래스"""


    def __init__(self,x=0,y=0): #Coordinate는 x,y값을 받는 클래스이고 self를 이용해 인스턴스마다 받을 수 있게함.
        self.x=x
        self.y=y

    def distance(self,point_2):  #어떤 인스턴스와 매개변수로 받을 다른 인스턴스 사이의 거리를 재는 함수. method이다.
        return math.sqrt(square(self.x - point_2.x) +
                         square(self.y - point_2.y))


def square(x):
    """전달받은 수의 제곱을 반환한다."""
    return x * x

class Shape:
    """도형을 나타내는 클래스"""

    sides=0 #sides를 초기화시켜놓았다. 밑의 describe method에서 self를 통해 그때그때 넣어준다.


    def describe(self): #이 method에서는 이 문장을 출력함.

        print("이 도형은",self.sides,"개의 변을 가지고 있습니다.")

class Triangle(Shape,Coordinate): #삼각형 클래스. Shape, Coordinate 클래스를 상속받는다. 겹치는 부분이 있을때는 Shape부터 확인함.
    sides=3 #하위클래스에서 재정의한다. Triangle안에서 정의되는 값이다.

    def __init__(self,point_a,point_b,point_c): #이 클래스의 속성이다. 세개의 매개변수를 self로 입력받는다.
        self.point_a=point_a
        self.point_b=point_b
        self.point_c=point_c

    def circumference(self): #이 method는 self로 받은 point들, 그리고 Coordinate의 distance method를 통해 이 method를 실행시킨다.
        return (self.point_a.distance(self.point_b)
                +self.point_b.distance(self.point_c)
                +self.point_c.distance(self.point_a))

class Rectangle(Shape):
    sides=4

    def __init__(self, point_a, point_b, point_c,point_d):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.point_d = point_d
    def circumference(self):
        return (self.point_a.distance(self.point_b)
                + self.point_b.distance(self.point_c)
                + self.point_c.distance(self.point_d)
                + self.point_d.distance(self.point_a))

shapes = [        #shapes라는 list를 만들어 안에 두 클래스를 넣고 값을 넣었다.
    Triangle(Coordinate(0,0),Coordinate(3,0),Coordinate(3,4)),
    Rectangle(Coordinate(2,2),Coordinate(6,2),Coordinate(6,6),Coordinate(2,6)),
]
for shape in shapes: #shapes라는 시퀀스를 1바퀴 순회하면서 shape라는 변수를 설정하여 각 list를 describe()를 출력한다.
    shape.describe()
    print("둘레",shape.circumference()) #위에서 사용한 shape라는 변수를 이용해 각 시퀀스마다의 둘레값을 출력한다.