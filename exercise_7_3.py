original_list=list(range(0,10))

result_list=[a*a for a in original_list]
print(result_list)

print(list(map(lambda n:n*n,original_list)))
total=0
def length(original_list):
    for a in original_list:
        n=(a + 1) / (a + 1)
        global total
        total=total+n
    print(total)
print(length(original_list))

fruits = ['배', '사과', '복숭아', '블루베리']
a = sorted(fruits, key=len, reverse=True)
print(a)

