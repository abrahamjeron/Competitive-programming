class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x = bin(x)[2:] 
        bin_y = bin(y)[2:] 
        max_len = max(len(bin_x), len(bin_y))
        og_x = bin_x.zfill(max_len)
        og_y = bin_y.zfill(max_len)
        print(og_x)
        print(og_y)
        distance = sum(1 for a, b in zip(og_x, og_y) if a != b)
        
        return distance