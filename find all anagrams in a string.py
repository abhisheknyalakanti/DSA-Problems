class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k=len(p)
        val=Counter(p)
        res=[]
        for i in range(len(s)-k+1):
            if Counter(s[i:i+k]) == val:
                res.append(i)
        return res