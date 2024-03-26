class Solution(object):
    def findRelativeRanks(self, score):
        score_sorted=sorted(score,reverse=True)
        d={}
        ans=[]
        print(score_sorted)
        for i in range(len(score_sorted)):
            if i==0:
                d[score_sorted[i]] = "Gold Medal"
            elif i==1:
                d[score_sorted[i]] = "Silver Medal"
            elif i==2:  
                d[score_sorted[i]] = "Bronze Medal"
            else:
                d[score_sorted[i]] = str(i+1) 
        for i in score:
            ans.append(d[i])
        return ans                
        