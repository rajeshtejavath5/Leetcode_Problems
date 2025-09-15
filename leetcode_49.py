# 49. Group Anagrams
# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.



#Approach -1
# strs=["eat","tea","tan","ate","nat","bat"]
# res=[]
# visited=[False]*len(strs)
# for i in range(len(strs)):
#     if visited[i]:
#         continue
#     first=strs[i]
#     sub=[first]
#     visited[i]=True
#     for j in range(i+1,len(strs)):
#         if visited[j]:
#             continue
#         second=strs[j]
#         if len(first)!=len(second):
#             continue
#         else:
#             for ch in second:
#                 if ch not in first:
#                     break
#             else:
#                 if first not in sub:
#                     sub.append(first)
#                 visited[j]=True
#                 sub.append(second)
#     if sub:
#         res.append(sub)
# for group in res:
#     group.sort()
# res.sort(key=lambda x: (len(x), x))
# print(res)



#################
def group_anagrams(strs):
    res = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in res:
            res[key] = []
        res[key].append(word)
    output = list(res.values())
    for group in output:
        group.sort()
    output.sort(key=lambda x: (len(x), x))
    return output
testcases = [
    ["eat","tea","tan","ate","nat","bat"],
    ["a", "b", "c", "a"],
    ["listen","silent","enlist","google","gooegl"],
    ["abc","bac","cab","xyz","zyx","yxz","def"],
    ["rat","tar","art","star","tars","cheese"],
    ["", ""],
    ["a gentleman", "elegant man"],
    ["Astronomer", "Moon starer"],
]
for item in testcases:
    print("input:",item)
    print("output: ",group_anagrams(item))
    print()

