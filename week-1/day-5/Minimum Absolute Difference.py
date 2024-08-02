class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res=[]
        min_diff=float(inf)
        for i in range(len(arr)-1):
             curr_diff=arr[i+1]-arr[i]
             if curr_diff<min_diff:
                 
                min_diff=curr_diff
                res=[[arr[i],arr[i+1]]]
             elif curr_diff == min_diff:
                res.append([arr[i],arr[i+1]])
        return res
        