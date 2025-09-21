# 459. Repeated Substring Pattern
# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false
# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.




def repeatedSubstringPattern(s):
    n=len(s)
    for i in range(1,n):
        if n%i==0:
            sub=s[:i]
            if sub*(n//i)==s:
                return True
    return False
testcases = [
    "abcabcabcabc",
    "aba",
    "abab",
    "abca",
    "aaaa",
    "a",
    "xyzxyz",
    "abcdabcdabcdabcd",
    "abababababab",
    "abcabcabcab",
    "zzzzzz",
    "abababx",
    "abcabcabcabcabcabc",
    "abcdabc",
    "ababababa",
    "abcabcxabcabc",
    "abcabcabcabcabcab",
    "aabbaabbaabb",
    "abcdabcdabce",
    "abcabcabcabcabcabcabcabc"
]
print("input:---------->output")
for item in testcases:
    print(f"{item}:------->{repeatedSubstringPattern(item)}")





















# s = "abac"
# def st(s):
#     res=[]
#     for i in range(len(s)):
#         for j in range(i+1,len(s)):
#             t=s[i:j]
#             print(t)
#             if len(t)>=1:
#                 res.append(t)
#     print(res)
#     for ch in res:
#         if res.count(ch)>1:
#             return True
#     else:
#         return False
# print(st(s))
