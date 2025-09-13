# 13. Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
def romantoint(s):
    d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    res=0
    prev=0
    for i in range(len(s)-1,-1,-1):
        value=d[s[i]]
        if value>=prev:
            res+=value
        else:
            res-=value
        prev=value
    return res


testcases = [
    "I",
    "IV",
    "IX",
    "XIV",
    "LVIII",
    "MCM",
    "MCMXCIV",
    "MMXXV",
    "MMMCMXCIX"
]
for item in testcases:
    print(item, "---->",romantoint(item))