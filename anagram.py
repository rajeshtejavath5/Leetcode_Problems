# # 3. Check for Anagrams
# # Example: "listen", "silent" → true
# # Question: Write a function to check if two strings are anagrams of each other.
# # Test Cases:
# # "listen", "silent" → true
# # "hello", "bello" → false
# # "race", "care" → true

# # "listen", "silent" → true


# # "hello", "bello" → false


# # "race", "care" → true


# # "a", "a" → true


# # "a", "b" → false


# # "aa", "aaa" → false (different lengths)


# # "" , "" → true (both empty)


# # "Debit Card", "Bad Credit" → true (ignoring spaces)


# # "School Master", "The Classroom" → true


# # "Astronomer", "Moon starer" → true


# sk="Astronomer"
# sl="Moon starer"
# s1,s2=sk.strip().lower(),sl.strip().lower()
# print(s1,s2)
# # def isanagram(s1,s2):
# #     if len(s1)!=len(s2):
# #         return False
# #     for ch in s1:
# #         if s1.count(ch)!=s2.count(ch):
# #             return False
# #     return True
# # obj=isanagram(s1,s2)
# # print(obj)

def are_anagram(words):
    if len(words)!=2:
        return False
    w1,w2=words
    w1=w1.replace(" ","").lower()
    w2=w2.replace(" ","").lower()
    if len(w1)!=len(w2):
        return False
    else:
        for ch in w1:
            if w1.count(ch)!=w2.count(ch):
                return False
        return True
    
testcases=[
    ("a","b"),
    ("aa","aaa"),
    ("race","Race"),
    ("School Master","The Classroom")]

for words in testcases:
    print(words,"--->" ,are_anagram(words))




# def q2(s):
#     stack = []
#     pairs = {')': '(', ']': '[', '}': '{'}
#     for ch in s:
#         if ch in "({[":
#             stack.append(ch)
#         elif ch in ")}]":
#             if not stack or stack[-1] != pairs[ch]:
#                 return False
#             stack.pop()
#     return not stack




