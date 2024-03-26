class Solution(object):
    def kthSmallest(self, matrix, k):
        ans=[]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                ans.append(matrix[i][j])
        ans.sort()
        return ans[k-1]        