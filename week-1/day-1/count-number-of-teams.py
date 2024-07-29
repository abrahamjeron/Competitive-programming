#difficulty level : medium
# leetcode link : https://leetcode.com/problems/count-number-of-teams/
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        higher_rating=[0]*len(rating)
        lower_rating=[0]*len(rating)
        count=0
        for i in range(len(rating)):
            for j in range(i+1,len(rating)):
                if rating[j]>rating[i]:
                    higher_rating[i]+=1
                elif rating[j]<rating[i]:
                    lower_rating[i]+=1
        for i in range(len(rating)):
            for j in range(i+1,len(rating)):
                if rating[j]>rating[i]:
                    count+=higher_rating[j]
                elif rating[j]<rating[i]:
                    count+=lower_rating[j]
        return count        