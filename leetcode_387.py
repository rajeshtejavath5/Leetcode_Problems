# 387. First Unique Character in a String
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1


# Constraints:
# 1 <= s.length <= 105
# s consists of only lowercase English letters.

# approach:1
def firstUniqChar1(s):
    for i in range(len(s)):
            count=0
            for j in range(len(s)):
                if s[i]==s[j]:
                    count+=1
            if count==1:
                return i
    return -1

#approach:2
def firstUniqChar2(s):
    for ch  in range(len(s)):
            if s.count(s[ch])==1:
                return ch
    return -1
     
#approach:3
def firstUniqChar3(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    for i,ch in enumerate(s):
        if freq[ch]==1:
            return i
    return -1

#approach 4:O(n),O(1) #Optimised
def firstUniqChar(s):
    freq=[0]*26
    for ch in s:
        freq[ord(ch)-ord('a')]+=1
    for i,ch in enumerate(s):
        if freq[ord(ch)-ord('a')]==1:
            return i
    return -1
testcases = [
    "leetcode",
    "loveleetcode",
    "aabb",
    "z",
    "abcabcdd",
    "aabbccdde",
    "racecar",
    "swiss",
    "success",
    "aaabcccdeeef",
    "aaaaaaaaaa",
    "abcdefghijklmnop",
    "zzzzzzzzzzzzzzzzzzzzzzzzzza",
    "ab" * 50 + "c"
]

print("Input:----------->Output")
for item in testcases:
    print(f"{item}----->{firstUniqChar(item)}")