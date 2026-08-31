class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        s=sorted(nums)
      
        
        l=[]
        for i in range(len(s)-2):
            if i>0 and s[i]==s[i-1]:
                continue
            left=i+1
            right=len(s)-1
            while left<right:
                sum=s[i]+s[left]+s[right]
                if sum<0:
                    left+=1
                elif sum>0:
                    right-=1
                else:
                    l.append([s[i],s[left],s[right]])
                    left+=1
                    right-=1
                    while left < right and s[left] == s[left - 1]:
                        left += 1

                    while left < right and s[right] == s[right + 1]:
                        right -= 1
                    
        return l


