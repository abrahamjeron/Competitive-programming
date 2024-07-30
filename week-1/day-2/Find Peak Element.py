# Difficulty level : Medium
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        for i in range(len(nums)):
            if (i == 0 or nums[i] > nums[i - 1]) and (i == len(nums) - 1 or nums[i] > nums[i + 1]):
                return i
        return -1