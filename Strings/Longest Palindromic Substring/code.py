class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pal(l,r):
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
            return s[l+1:r]
        longest=""
        for i in range(len(s)):
            st1 = pal(i, i + 1)
            st2=pal(i,i)
            if len(st1)>len(longest):
                longest=st1
            if len(st2)>len(longest):
                longest=st2
        return longest

        


            
        return longest