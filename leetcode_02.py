# 1. Two Sum
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]




class Solution:
    def twoSum(self, nums, target):
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        #########################
        # nums.sort()
        # left=0
        # right=len(nums)-1
        # while left<right:
        #     current_sum1 = nums[left] +  nums[right]
        #     if current_sum1==target:
        #         return [left,right]
        #     elif current_sum1<target:
        #         left+=1
        #     else:
        #         right-=1
        # return []
        ################
        seen={}
        for i,num in enumerate(nums):
            c=target-num
            if c in seen:
                return [seen[c],i]
            else:
                seen[num]=i
        return []
    
# nums=[2,7,11,15]
nums=list(map(int,input("enter values : ").split()))
target=9
obj=Solution()
result=obj.twoSum(nums,target)
print(result,"returnde indices of nums")