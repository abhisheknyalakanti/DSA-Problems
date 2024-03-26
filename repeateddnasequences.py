class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen=set()
        res=set()
        for i in range(len(s)-9):
            substring=s[i:i+10]
            if substring in seen:
                res.add(substring)
            seen.add(substring)
        return list(res)        
        