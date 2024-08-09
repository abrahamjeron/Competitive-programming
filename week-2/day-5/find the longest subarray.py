n=int(input())
nums=list(map(int,input().split()))
curr_max=global_max=nums[0]
for num in nums:
    curr_max=max(num,curr_max+num)
    global_max=max(curr_max,global_max)
print(global_max)
