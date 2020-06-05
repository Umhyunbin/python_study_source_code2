exercise_list=[1,3,5,7,9]
cent=int((len(exercise_list)-1)/2)

def center(cent):

    n=exercise_list[cent]
    return n
print(center(cent))

mirror_list=exercise_list[3::-1]
def mirror():
    plus_list=exercise_list+mirror_list
    A=print(plus_list)
    return A
mirror()

def minmax():
    minmax=[min(exercise_list),max(exercise_list)]
    print(minmax)
minmax()

def mean():
    average=float((sum(exercise_list)/len(exercise_list)))
    print(average)
mean()

range(0,10000,2)
sum_range=sum(range(0,10000,2))
print(sum_range)

m_list=list(range(9,-1,-1))
print(m_list)

