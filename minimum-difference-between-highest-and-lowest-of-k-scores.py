class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)<=1:
            return 0
        nums.sort()
        d=float("inf")
        n=len(nums)
        for i in range(n-k+1):
            s = abs(nums[i]- nums[i+k-1])
            d=min(s,d)
        return d
