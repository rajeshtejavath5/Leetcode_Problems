# 451. Sort Characters By Frequency
# Given a string s, sort it in decreasing order based on the frequency of the characters.
# The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.

# Example 1:
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Example 2:
# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.

# Example 3:
# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
 

# Constraints:

# 1 <= s.length <= 5 * 105
# s consists of uppercase and lowercase English letters and digits.


################
# code
# Approach 1:

# class Solution(object):
#     def frequencySort(self, s):
#         dic={}
#         for ch in s:
#             if ch not in dic:
#                 dic[ch]=1
#             else:
#                 dic[ch]+=1
#         temp=dic.copy()
#         res=""
#         while temp:
#             max_value=float('-inf')
#             max_key=None
#             for k,v in temp.items():
#                 if v>max_value:
#                     max_value=v
#                     max_key=k
#             res+=str(max_key)*max_value
#             del temp[max_key]
#         return res
# obj=Solution()
# testcases = [
#     "Aabb",
#     "cccaaa",
#     "tree",
#     "89880",
#     "a",
#     "aaaaaa",
#     "abcdef",
#     "bbbaaacccddd",
#     "PythonRocks",
#     "1122334455",
#     "!!!@@@",
#     "aAaAaA",
#     "zzzYYYxxx",
#     "longlonglong"
# ]
# print("input------>output")
# for item in testcases:
#     print(f"{item}------->{obj.frequencySort(item)}")



##########
# Approach2
from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        count = Counter(s)
        max_freq = max(count.values())
        buckets = [[] for _ in range(max_freq + 1)]

        for ch, freq in count.items():
            buckets[freq].append(ch)

        res = []
        for freq in range(max_freq, 0, -1):
            for ch in buckets[freq]:
                res.append(ch * freq)

        return "".join(res)
obj=Solution()
testcases = [
    "Aabb",
    "cccaaa",
    "tree",
    "89880",
    "a",
    "aaaaaa",
    "abcdef",
    "bbbaaacccddd",
    "PythonRocks",
    "1122334455",
    "!!!@@@",
    "aAaAaA",
    "zzzYYYxxx",
    "longlonglong"
]
print("input------>output")
for item in testcases:
    print(f"{item}------->{obj.frequencySort(item)}")
