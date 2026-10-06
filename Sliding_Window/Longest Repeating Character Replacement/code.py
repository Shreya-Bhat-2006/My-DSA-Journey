class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        l=0
        maxi=0
        cur=0
        for r in range(len(s)):
            d[s[r]]=d.get(s[r],0)+1
            maxi=max(d.values())
            w=r-l+1
            while w-maxi>k:
                d[s[l]]-=1
                l+=1
                w=r-l+1
                maxi=max(d.values())
            cur=max(cur,w)
        return cur
            
