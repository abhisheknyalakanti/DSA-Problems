class solution:
    def makeSmallestPalindrome(self,s:str)->str:
        n=len(s)
       ans=" "
       for i in range(n):
           print(s[i],s[n-i-1],min(s[i],s[n-i-1]))
           ans+=min(s[i],s[n-i-1])
      return ans    