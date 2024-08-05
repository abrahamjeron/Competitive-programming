class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count=collections.defaultdict(int)
        l,tot,res=0,0,0
        for r in range(len(fruits)):
            count[fruits[r]]+=1
            tot+=1
            while len(count)>2:
                f=fruits[l]
                count[f]-=1
                tot-=1
                l+=1
                if not count[f]:
                    count.pop(f)
            res=max(res,tot)
        return res
