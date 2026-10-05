class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l=0
        c=0
        maxi=0
        for r in range(len(nums)):
            
            if nums[r]==0:
                c+=1

            
            while c>k:
                if nums[l]==0:
                    l+=1
                    c-=1
                else:
                    l+=1
                    
            valid=r-l+1
                    


            if valid>maxi:
                maxi=valid

        return maxi
            
            