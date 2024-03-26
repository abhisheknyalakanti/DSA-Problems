
Class Solution:
    def findLHS(self, nums: List[int]) -> int:
        maxlength=0
        freq=Counter(nums)
        for key in freq:
            if key+1 in freq:
                maxlength=max(maxlength,freq[key]+freq[key+1])
        return maxlength        


