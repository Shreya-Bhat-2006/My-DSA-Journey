class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        d={}
        for i in nums1:
            d[i]=d.get(i,0)+1
        for num in nums2:
            if num in d and d[num]>0:
               l.append(num)
               d[num]-=1
        return l