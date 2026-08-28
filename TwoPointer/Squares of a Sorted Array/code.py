class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        pos=r
        l1=[0]*len(nums)
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
               
                l1[pos]=nums[l]*nums[l]
                l+=1
                pos-=1
            else:
                l1[pos]=nums[r]*nums[r]
                r-=1
                pos-=1
        
        return l1


            
