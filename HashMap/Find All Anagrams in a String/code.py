class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d1={}
        d2={}
        l=0
        r=0
        L=[]
        for i in p:
            d2[i]=d2.get(i,0)+1
        
        while r<len(s):
            d1[s[r]] = d1.get(s[r], 0) + 1
            if r - l + 1 == len(p):
                if d1==d2:
                    L.append(l)
                d1[s[l]]-=1
                if d1[s[l]] == 0:
                    del d1[s[l]]
                l+=1
            r+=1
        return L
                       
            