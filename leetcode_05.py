# 5. Longest Palindromic Substring

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

def is_palindrome(s1):
    left=0
    right=len(s1)-1
    while left<right:
        if s1[left]!=s1[right]:
            return False
        left+=1
        right-=1
    return True

s=input("enter the string : ")
longest=""
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        res=s[i:j]
        if is_palindrome(res) and len(res)>len(longest):
            longest=res
print(f"Longest Palindromic Substring : {longest}")