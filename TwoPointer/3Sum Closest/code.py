class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
     
        cur=0
        close = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)-2):

            l=i+1
            r=len(nums)-1
            while l<r:
                cur=nums[i]+nums[l]+nums[r]
                if (abs(target-cur)<abs(target-close)):
                    close=cur
                if cur<target:
                    l+=1
                elif cur>target:
                    r-=1
                else :
                    return cur
        return close