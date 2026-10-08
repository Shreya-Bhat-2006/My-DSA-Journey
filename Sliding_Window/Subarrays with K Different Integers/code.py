class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atmost(k):
            s={}
            l=0
            ans=0
            for r in range (len(nums)):
                s[nums[r]]=s.get(nums[r],0)+1
                while len(s)>k:
                    s[nums[l]]-=1
                    if s[nums[l]]==0:
                        del(s[nums[l]])
                    l+=1
                ans+=r-l+1
            return ans
        return atmost(k)-atmost(k-1)