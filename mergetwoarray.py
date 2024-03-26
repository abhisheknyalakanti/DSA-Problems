class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        p1,p2=0,0
        res=[]
        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1][0]==nums2[p1][0]:
                res.append([nums1[p1][0],nums1[p1][1]+nums2[p2][1]])
                p1+=1
                p2+=1
            elif nums1[p1][0]>nums2[p1][0]:
                res.append([nums2[p2][0],nums2[p2][1]])
                p2+=1
            else:
                res.append([nums2[p1][0],nums1[p1][1]])
                p1+=1
        for i in range(p1,len(nums1)):
            res.append(nums1[i])
        for i in range(p2,len(nums2)):
            res.append(nums2[i]) 
        return res                     
        