# 14. Longest Common Prefix
# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# strs = ["flower","flow","flight"]

##########################

# strs = ["flower","","flight"]
# if len(strs[0])==0:
#     print("no common prefix")
# else:
#     first=strs[0]
#     result=""
#     stop=False
#     for i in range(len(first)):
#         letter=first[i]
#         for word in strs:
#             if i>=len(word) or  letter!=word[i]:
#                 # print(result)
#                 stop=True
#                 break
#         if stop:
#             break
#         result+=letter
#     print(result,len(result))
    

##########################
# def common_prefix(l):
#     l.sort()
#     if not l or len(l[0])==0:
#         return "no common prefix"
#     first=l[0]
#     last=l[-1]
#     i=0
#     while i<len(first) and i<len(last) and first[i]==last[i]:
#         i+=1
#     return first[:i]

# testcases=[ ["flower","flow","flight"],
#            ["dog","racecar","car"],
#            [""],
#            [],
#            ["rajesh","rajesh","rajesh"]
#             ]
# for item in testcases:
#     print(f"{item}common prefix--->{common_prefix(item)}")
        

