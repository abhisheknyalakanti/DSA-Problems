class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=sum=(nums[:k])
        n=len(nums)
        answer=s
        for i in range((k,n):
            s+=nums[i]
            s-=nums[i-k]
            answer=max(answer,s)
        return answer/k    

                 
        
        