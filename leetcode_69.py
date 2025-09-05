#sep04
# leetcode: 69
#cube root problem......
# inputs:   -27  --> -3 (output)
        #   1000 --> 10
        #   -125  --> -5
        #   6859  --> 19
        #   -19683 --> -27
# def cuberoot(n):
#     s=abs(n)
#     l=0
#     h=s
#     while l<=h:
#         mid=(l+h)//2
#         if mid*mid*mid==s:
#             return mid
#         elif mid*mid*mid>s:
#             h=mid-1
#         else:
#             l=mid+1
#     if n<0:
#         return -mid
#     else:
#         return mid
# print(cuberoot(-1000))


# import math
# def cuberoot(n):
#     s=abs(n)
#     l=0
#     h=s
#     while l<=h:
#         mid=(l+h)/2
#         if mid*mid==s:
#             return math.floor(mid)
#         elif mid*mid>s:
#             h=mid-1
#         else:
#             l=mid+1
#     if n<0:
#         return math.floor(-mid)
#     else:
#         return math.floor(mid)
# print(cuberoot(8))








#-27  --> -3 (output)
        #   1000 --> 10
        #   -125  --> -5
        #   6859  --> 19
        #   -19683 --> -27

# n=-19683
# s=abs(n)
# res=-1
# for i in range(s):
#     if i*i*i==s:
#         res=i
#         break
# if n<0:
#     print(-(res))
# else:
#     print(res)