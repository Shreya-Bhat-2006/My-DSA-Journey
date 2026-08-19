class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d1={}
        d2={}
        for i in t:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1

        left=0
        right=0
        
        st=""
        while right<len(s):
            valid=True
            d1[s[right]]=d1.get(s[right],0)+1
            right+=1
            for key,value in d2.items():
                if d1.get(key,0)<value:
                   valid=False
                   break
            
                
            while valid:
                if st == "" or right - left < len(st):
                   st = s[left:right]
                
                d1[s[left]]-=1
                left+=1
                valid=True
                for key,value in d2.items():
                    if d1.get(key,0)<value:
                       valid=False
                       break
        return st



               

                
        
               
        
              

              


