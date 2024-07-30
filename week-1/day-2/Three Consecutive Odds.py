# Difficulty level : Medium
# Bruteoforce Method:
# class Solution:
#     def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # for i in range(len(arr)-2):
        #     if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0:
        #         return True

# Optimal solution:
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:   
        count=0
        for num in arr:
            if num%2!=0:
                count+=1
                if count==3:
                    return True
            else:
                count=0
        return False  