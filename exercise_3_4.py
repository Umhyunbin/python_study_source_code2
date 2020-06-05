pi = 3.141592653589793

def area_of_circle(radius):
    """원의 반지름(radius)을 입력받아 넓이를 반환한다."""
    area = radius * radius * pi
    return area

def volume_of_cylinder(radius, height):
    """원기둥의 반지름(radius)과 높이(height)를 입력받아
    부피를 반환한다."""
    top_area = area_of_circle(radius)
    volume = top_area * height
    return volume

result = volume_of_cylinder(5, 10)
print(result)
#전역변수 : pi,result
#지역변수 : radius(area함수 매개변수),area////radius(volume함수 매개변수),height,top_area,volume


