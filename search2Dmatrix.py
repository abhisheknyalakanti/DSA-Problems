class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            r=len(matrix[i])-1
            l=0
            arr=matrix[i]
            check=True
            if target>arr[len(arr)-1]:
                check=false
            while l<=r and check:
                mid=l+(r-l)//2
            if arr[mid]==target:
                return True
            elif arr[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return false            

