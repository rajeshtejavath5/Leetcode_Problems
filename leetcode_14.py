# 14. Longest Common Prefix
# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# strs = ["flower","flow","flight"]
first=strs[0]
result=""
stop=False
for i in range(len(first)):
    letter=first[i]
    for word in strs:
        if i>=len(word) or  letter!=word[i]:
            # print(result)
            stop=True
            break
    if stop:
        break
    result+=letter
if result:
    print(f"longst common prefix is : {result}")
else:
    print("no longest common prefix")
        

