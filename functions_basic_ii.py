#1
def countdown(x):
    list=[]
    for i in range(x,-1,-1):
        list.append(i)
    return list
print(countdown(8))

#2
def print_and_return(secondList):
    print(secondList[0])
    return(secondList[1])
print(print_and_return([8,30]))

#3
def first_plus_length(thirdList):
    print(thirdList[0])
    return len(thirdList)
print(first_plus_length([5,5,5]))

#4 - NOT COMPLETE
def values_greater_than_second(fourthList):
    if len(fourthList)<2:
        return False
    list=[]
    for y in list:
        if y>list[1]:
            list.append(y)
    print(len(list))
    return list
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([1]))

#5
def length_and_value(length,value):
    list = []
    for a in range(length):
        list.append(value)
    return list
print(length_and_value(5,7))