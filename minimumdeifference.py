class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if n<=1:
            return 0
        nums.sort()
        d=float('inf')
        for i in range((n-k)+1):
            diff=abs(nums[i]-nums[i+k-1])
            d=min(diff,d)
        return d        
            
        