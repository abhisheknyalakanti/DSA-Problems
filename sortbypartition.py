class Solution(object):
    def sortArrayByParity(self, nums):
        l=0
        for i in range(len(nums)):
            if (nums[i]%2==0):
                nums[l],nums[i]=nums[i],nums[l]    
                l+=1         
        return nums
                