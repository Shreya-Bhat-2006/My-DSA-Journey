class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        s=set()
        
        maxi=0
        left=0
        cur_sum=0
        for right in range(len(nums)):
            while nums[right]  in s:
                s.remove(nums[left])
                cur_sum-=nums[left]
                left+=1
                
                
        
            
            s.add(nums[right])
            cur_sum+=nums[right]             
            if right-left+1==k:
                if maxi<cur_sum:
                    maxi=cur_sum
                s.remove(nums[left])
                cur_sum-=nums[left]
                left+=1

                
                


                    
                
                

        
        return maxi
            

       
