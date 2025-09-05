# leetcode problem : 540
####unique element:
# i/p   arr=[1,1,2,2,3,4,4]
# even ki right
# odd ki left side duplicate value
# arr=[1,1,2,2,3,4,4]
# def unique(arr):
#     left=0
#     right=len(arr)-1
#     res=-1
#     if arr[-1]!=arr[-2]:
#         return arr[-1]
#     elif arr[0]!=arr[1]:
#         return arr[0]
#     while left<=right:
#         mid=(left+right)//2
#         if arr[mid]!=arr[mid+1] and arr[mid]!=arr[mid-1]:
#             return arr[mid]
#         elif mid%2!=0:
#             if arr[mid]==arr[mid-1]:
#                 left=mid+1
#             else:
#                 right=mid-1
#         elif mid%2==0:
#             if arr[mid]==arr[mid+1]:
#                 left=mid+1
#             else:
#                 right=mid-1
#     return res
# print(unique(arr))





# arr=[1,1,2,2,3,3,4,4,5]
# freq={}
# for i in arr:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# print(freq)
# for k,v in freq.items():
#     if v==1:
#         print(k)
#     # print("there is no unique")



arr=[1,1,2,2,3,4,4,5,5]
def unique(arr):
        i=0
        while i<len(arr):
                if len(arr)-1==i:
                        return arr[i]
                if arr[i]==arr[i+1]:
                        i+=2
                else:
                        return arr[i]
print(unique(arr))  