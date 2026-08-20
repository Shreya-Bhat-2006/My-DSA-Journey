class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ps=0
        
        
        d={0:-1}
        for i in range(len(nums)):
            ps+=nums[i]
            r=ps%k
            if r in d:
                if i-d[r]>=2:
                    return True
            else:
                d[r]=i
        
       
            
        
        return False
        