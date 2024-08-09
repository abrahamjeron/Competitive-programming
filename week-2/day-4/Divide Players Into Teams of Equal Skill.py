class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # for finding the common value 
        skill.sort()
        # x=len(skill)//2
        commonvalue=skill[0]+skill[-1]
        chem_multiples=[]
        l,r=1,len(skill)-2
        while l<r:
            current_commonvalue=skill[l]+skill[r]
            if current_commonvalue != commonvalue:
                return -1
            chem_multiples.append(skill[l]*skill[r])
            l+=1
            r-=1
        # For finding the number pairs whose sum is equal to the commonvalue (target in two sum)
        L,R=0,len(skill)-1
        while L<R:
            if skill[L]+skill[R]==commonvalue:
                chem_multiples.append(skill[L]*skill[R])
            elif skill[L]+skill[R]<commonvalue:
                l+=1
            else:
                r-=1
            break
        # print(chem_multiples)
        return sum(chem_multiples)
        # [3,2,5,1,3,4]
        # [1,2,3,3,4,5]
        # 0,3,5,6,