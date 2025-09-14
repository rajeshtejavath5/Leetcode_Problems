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
# def isanagram(s1,s2):
#     if len(s1)!=len(s2):
#         return False
#     for ch in s1:
#         if s1.count(ch)!=s2.count(ch):
#             return False
#     return True
# obj=isanagram(s1,s2)
# print(obj)

############################

def is_anagram(words):
    s1,s2=words
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()
    if len(s1)!=len(s2):
        return False
    count={}
    for ch in s1:
        if ch not in count:
            count[ch]=1
        else:
            count[ch]+=1
    for ch in s2:
        if ch not in count:
            return False
        count[ch]-=1
        if count[ch]<0:
            return False
    return True

testcases = [
    ("aacc","ccac"),
    ("a", "b"),
    ("aa", "aaa"),
    ("race", "Race"),
    ("School Master", "The Classroom"),
    ("Astronomer", "Moon starer"),
    ("Debit Card", "Bad Credit"),
    ("listen", "silent"),
    ("triangle", "integral"),
    ("rat", "car"),
    ("", ""),
    ("a gentleman", "elegant man"),
    ("Clint Eastwood", "Old West Action"),
    ("William Shakespeare", "I am a weakish speller"),
    ("dormitory", "dirty room"),
    ("the eyes", "they see"),
    ("hello", "billion")
]
for item in testcases:
    print(item ,"----->" ,is_anagram(item))
    



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


# "School Master","The Classroom"
# "Astronomer", "Moon starer"

# s1="Astronomer"
# s2="Moon starer"
# s3,s4=s1.lower(),s2.lower()
# for i in s4:
#     if i not  in s3:
#         print("not anagram")
#         break
# else:
#     print("anagram yesss")