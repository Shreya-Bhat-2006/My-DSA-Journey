class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        target=k*threshold
        ws=sum(arr[:k])
        c=0
        if ws>=target:
            c+=1
        for i in range(k,len(arr)):
            ws+=arr[i]
            ws-=arr[i-k]
            if ws>=target:
               c+=1
        return c
        

