# 3. Longest Substring Without Repeating Characters

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def get_sub_strings(s):
    ans=[]
    for i in range(len(s)):
        for j in range(i,len(s)+1):
            res=s[i:j+1]
            if len(set(res))==len(res): 
                # if res not in ans:     #this line removes duplicate substring item 
                ans.append(res)
    return ans   
text=input("enter a string :")
unique_sub_strings=get_sub_strings(text)
# print(sub_strings)  #here we can unique or non repeating possible strings from given input string
longest=""
for item in unique_sub_strings:
    if len(item)>len(longest):
        longest=item
print(longest)
    
            
