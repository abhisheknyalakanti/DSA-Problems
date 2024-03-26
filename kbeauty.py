class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        count=0
        for i in range(k,len(s)+1):
            div=int(s[i-k:i])
            if div!=0 and num%div==0:
                count+=1
        return count        


        