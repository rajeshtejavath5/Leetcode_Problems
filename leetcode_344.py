# 344. Reverse String

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.


# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


#brute force:
# s= ["H","a","n","n","a","h"]
# res=[]
# for i in range(len(s)-1,-1,-1):
#     res.append(s[i])
# print(res)

########################

def reverse_string(s):
    l=0
    r=len(s)-1
    while l<r:
        s[l],s[r]=s[r],s[l]
        l+=1
        r-=1
    return s

test_cases=[["H","a","n","n","a","h"],
            ["h","e","l","l","o"]]

for item in test_cases:
    print(f"{item}------->{reverse_string(item)}")

