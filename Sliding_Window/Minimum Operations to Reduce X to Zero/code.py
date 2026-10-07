class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target=sum(nums)-x
        if target<0:
            return -1
        if target==0:
            return len(nums)
        l=0
        maxi=-1
        summ=0
        for r in range(len(nums)):
            summ+=nums[r]
            while summ>target:
                summ-=nums[l]
                l+=1
            if summ==target:
                maxi=max(maxi,r-l+1)
        if maxi==-1:
            return -1
        return (len(nums)-maxi)