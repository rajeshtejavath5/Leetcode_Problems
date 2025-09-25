#Bubble Sort
# 1. Implement Bubble Sort (Ascending Order)
def Ascending_order(lst):
    for i in range(len(lst)):
        for j in range(0,len(lst)-1-i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
lst = list(map(int, input("enter your list of elements: ").split()))
print(Ascending_order(lst))

# 2. Bubble Sort in Descending Order
def Descending(lst):
    for i in range(len(lst)):
        for j in range(0,len(lst)-1-i):
            if lst[j]<lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
lst = list(map(int, input("enter your list of elements: ").split()))
print(Descending(lst))

# 3.Optimize Bubble Sort (Early Stopping)
def optimised_bubble_sort(lst):
    for i in range(len(lst)):
        swapped=False
        for j in range(0,len(lst)-1-i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                swapped=True
        if not swapped:
            return lst
    return lst
lst = list(map(int, input("enter your list of elements: ").split()))
print(optimised_bubble_sort(lst))

# 4.Count Number of Swaps

def swaps_count(lst):
    count=0
    for i in range(len(lst)):
        for j in range(0,len(lst)-1-i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                count+=1
    return lst,count
lst = list(map(int, input("enter your list of elements: ").split()))
print(swaps_count(lst))

# 5.Sort Strings Using Bubble Sort

def strings_bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(0,len(lst)-1-i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
lst=list(input("enter your list of elements:-").split())
print(strings_bubble_sort(lst))







