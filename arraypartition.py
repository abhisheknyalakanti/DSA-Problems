class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        total=0
        for i in range(len(nums)):
            if (i+1)%2==1:
                total+=nums[i]
        return total  