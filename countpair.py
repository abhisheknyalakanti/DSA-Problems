class Solution(object):
    def countPairs(self, nums, target):
        n=len(nums)
        nums.sort()
        l=0
        r=n-1
        no_of_pairs=0
        while l<r:
            if nums[l] + nums[r] < target:
                no_of_pairs+=r-l
                l+=1
            else:
                r-=1
        return no_of_pairs                 