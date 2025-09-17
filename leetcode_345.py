# 345. Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"

# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

# Approach:1
# def rev_vowels_in_s(s):
#     vowels='aeiouAEIOU'
#     vowel_set=[]
#     for ch in s:
#         if ch in vowels:
#             vowel_set.append(ch)
#     lst=list(s)
#     vowel_set.reverse()
#     vowel_index=0
#     for i in range(len(lst)):
#         if lst[i] in vowels:
#             lst[i]=vowel_set[vowel_index]
#             vowel_index+=1
#     return "".join(lst)
# print(rev_vowels_in_s("leetcode"))


#Approach 2
def rev_vowels_in_s(s):
    lst=list(s)
    l=0
    r=len(lst)-1
    vowels='aeiouAEIOU'
    while l<r:
        if lst[l] in vowels and lst[r] in vowels:
            lst[l],lst[r]=lst[r],lst[l]
            l+=1
            r-=1
        elif lst[l] not in vowels:
            l+=1
        elif lst[r] not in vowels:
            r-=1
    return "".join(lst)

test_cases = [
    "leetcode",
    "IceCreAm",
    "",
    "rhythm",
    "AEIOUaeiou",
    "a",
    "b",
    "racecar",
    "Programming",
    "HELLOworld",
]
for i in test_cases:
    print(f"{i}---->{rev_vowels_in_s(i)}")