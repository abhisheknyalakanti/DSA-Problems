class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        count=0
        i=0
        Sum=0
        ans=0
        s=set()
        for j in range(len(nums)):
            while nums[j] in s:
                s.remove(nums[i])
                Sum-=nums[i]
                i+=1
            s.add(nums[j])
            Sum+=nums[j]
            ans = max(ans,Sum)
        return ans
            
