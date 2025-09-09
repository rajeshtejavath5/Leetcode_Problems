# 28. Find the Index of the First Occurrence in a String
# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.


class Solution(object):
    def strStr(self, haystack, needle):
        # return haystack.find(needle)
        n=len(haystack)
        m=len(needle)
        for i in range(n):
            if haystack[i:i+m]==needle:
                return i
        return -1
s=input("Enter Haystack:")
n=input("Enter Needle:")
res=Solution()
print(res.strStr(s,n))

        