class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        cur_sum=0
        l=0
        Len=float("inf")
        for r in range(len(nums)):
            cur_sum+=nums[r]
           
            while cur_sum>=target:
                Len=min(Len,r-l+1)
                cur_sum-=nums[l] 
                l+=1
        if Len==float("inf"):
            return 0


        return Len