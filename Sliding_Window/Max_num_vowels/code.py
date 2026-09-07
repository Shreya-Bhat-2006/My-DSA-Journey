class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        c=0
        l=0
        r=0
        maxi=0
        d={'a', 'e', 'i', 'o','u'}
        for i in s:
            r+=1
            if r-l<=k:
                if i in d:
                    c+=1
            else:
                if s[l] in d:
                    c-=1
                l+=1
                if i in d:
                   c+=1
            if r-l == k:
                maxi = max(maxi, c)
                
        return maxi
            

                