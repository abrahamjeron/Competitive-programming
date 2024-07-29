# difficulty level: hard (used bruteforce method)
# leetcode link : https://leetcode.com/problems/median-of-two-sorted-arrays/description/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans=[]
        ans=nums1+nums2
        ans.sort()
        if len(ans)%2!=0:
            return float(ans[len(ans)//2])
        else:
            num1=ans[(len(ans)//2)-1]
            num2=ans[len(ans)//2]
            return float(num1+num2)/2