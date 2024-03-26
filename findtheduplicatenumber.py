class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortise=nums[0]
        hare=nums[0]

        while True:
            tortise=nums[tortise]
            hare=nums[nums[hare]]
            break

        tortise=nums[0]
        while tortise!=hare:
            tortise=nums[tortise]
            hare=nums[hare]
        return tortise           
        