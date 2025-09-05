s=5
n=(s**2)-((s-1)*(s)//2)  #10 values 
lst=[]
a=0
b=1
for i in range(n):
    c=a+b
    lst.append(a)
    a=b
    b=c
print(lst)


index=0
for i in range(1,s+1):
    start=s-1
    for j in range(1,i+1):
        print(lst[index],end=" ")
        index+=start
        start-=1
    index=i
    print()


# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
# 0 
# 1 5 
# 1 8 34 
# 2 13 55 144 
# 3 21 89 233 377