# Difficulty level : Medium
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        res = 0
        for p1 in points:
            angles = {}
            max = 0
            same_points = 0
            for p2 in points:
                if p1 == p2:
                    same_points += 1
                    continue

                if p1[0] == p2[0]:
                    angle = float("inf")
                else:
                    angle = (p1[1] - p2[1]) / (p1[0] - p2[0])
                angles[angle] = angles.get(angle, 0) + 1
                if max < angles[angle]:
                    max = angles[angle]
            if res < max + same_points:
                res = max + same_points

        return res