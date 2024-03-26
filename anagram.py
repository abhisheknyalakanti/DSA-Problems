class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k=len(p)
        pvalue=Counter(p)
        res=[]
        for i in range(len(s)-k+1):
            if Counter(s[i:i+k])==pvalue:
                res.append(i)
        return res                    

            