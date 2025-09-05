# 20. Valid Parentheses
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Example 5:
# Input: s = "([)]"
# Output: false

# open_c=close_c=f_open_c=f_close_c=s_open_c=s_close_c=0
# # s=input("enter the string: ")
# s="[]{}{({})}"
# for i in range(len(s)):
#     if s[i]=="(":
#         open_c+=1
#     elif s[i]==")":
#         close_c+=1
#     elif s[i]=="{":
#         f_open_c+=1
#     elif s[i]=="}":
#         f_close_c+=1
#     elif s[i]=="[":
#         s_open_c+=1
#     elif s[i]=="]":
#         s_close_c+=1
# if open_c==close_c and f_open_c==f_close_c  and s_open_c==s_close_c:
#     print("valid")
# else:
#     print("not valid")



def valid(s):
    mem=[]
    for i in s:
        c=i
        if i in "({[":
            mem.append(i)
        elif i in ")}]":
            if len(mem)==0:
                return False
            top=mem.pop()
            if not (top=="(" and c==")" or 
                top=="{" and c=="}" or
                top=="[" and c=="]" ):
                return False
        # else:
            # return False     #because to work on this type of inpu also   abc--> valid 
    return len(mem)==0

tests = [
    "()",
    "({})",
    "()[]",
    "([])",
    "({[]})",
    "([)]",
    "(((",
    "{[()]}",
    "[(])",
    "(){[]}",
    "([{}])",
    "((()))",
    "{([])}",
    "abc"
]

for i in tests:
    print(f"{i:10s}--> {'valid' if valid(i) else 'invalid' }")

    