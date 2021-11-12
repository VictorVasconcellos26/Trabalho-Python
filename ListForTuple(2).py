numbers = []
for c in range(10):
    numbers.append(int(input('Digite um numero: ')))

list1 = 0
list2 = 0

def ListFoRTuple(list1, list2):
    for x in numbers:
        if x > 0:
            list1 = list1 + 1
        else:
            list2 = list2 + 1
    return list1, list2
print(ListFoRTuple(list1,list2))