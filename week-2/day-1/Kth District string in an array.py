class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count=collections.defaultdict(int)
        for char in arr:
            count[char]+=1
        val=[]
        for char in count:
            if count[char]==1:
                val.append(char)
        if k <= len(val):
            return val[k-1]
        else:
            return ""
        