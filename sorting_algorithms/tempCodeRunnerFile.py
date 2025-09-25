def Ascending_order(lst):
    for i in range(len(lst)):
        for j in range(0,len(lst)-1-i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
lst = list(map(int, input("enter your list of elements: ").split()))
print(Ascending_order(lst))