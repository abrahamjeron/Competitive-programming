def find_judge(trust,n):
    if n==1:
        return 1
    trust_count=[0]*(n+1)
    trusted_count=[0]*(n+1)
    for a,b in trust:
        trust_count[b]+=1
        trusted_count[a]+=1
    for person in range(1,n+1):
        if trust_count[person]==n-1 and trusted_count[person]==0:
            return person
    return -1
nums_trust=int(input())
n=int(input())
trust=[list(map(int,input().split())) for _ in range(nums_trust)]
