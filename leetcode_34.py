arr=[1,2,3,4,5,5,5,6]
target=5
def first_occurance(arr,target):
    left=0
    right=len(arr)-1
    result=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            result=mid
            right=mid-1
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return result
def last_occurance(arr,target):
    left=0
    right=len(arr)-1
    result=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            result=mid
            left=mid+1
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return result

print(first_occurance(arr,target))
print(last_occurance(arr,target))





