mult_3=list(set(range(0,1000,3)))
mult_4=list(set(range(0,1000,4)))
sum=int(len(mult_3))+int(len(mult_4))
print(sum)

weekday={'mon','tues','wen','thurs','fri'}
weekend={'sat','sun'}

n=input()
def is_working_day(n):
    rest= n in weekend
    print(rest)
is_working_day(n)