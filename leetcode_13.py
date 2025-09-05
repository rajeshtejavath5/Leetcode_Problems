# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

text="II"
res=[]
d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
for v in d:
    for ch in text:
        if d[v]==ch:
            res.append(ch)
print(res)