class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        d={}
        l=0
        maxi=0
        for r in range(len(fruits)):
            d[fruits[r]]=d.get(fruits[r],0)+1
            while len(d)>2:
                d[fruits[l]]-=1
                if d[fruits[l]]==0:
                    del d[fruits[l]]
                l+=1
            cur=r-l+1
            maxi=max(cur,maxi)
        return maxi