class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        ans=0
        rem=0 
        curem=0 
        comp= nums[n-1] 
        for i in range(n-2,-1,-1):
            if(nums[i]<comp): 
                comp=nums[i] 
                rem+=curem 
                curem=0 
                ans+=1
            elif(nums[i]==nums[i+1]): 
                if(rem>0):
                    rem-=1
                    ans+=1
                curem+=1 
        return ans