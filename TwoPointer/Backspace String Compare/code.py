class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
       
        r1=len(s)-1
        r2=len(t)-1
        sk1=0
        sk2=0
        while r1>=0 or r2>=0:
            while r1>=0:
                if s[r1]=="#":
                    sk1+=1
                    r1-=1
                elif sk1>0:
                    sk1-=1
                    r1-=1
                else:
                    break

            while r2>=0:
                if t[r2]=="#":
                    sk2+=1
                    r2-=1
                elif sk2>0:
                    sk2-=1
                    r2-=1
                else:
                    break
            if r1>=0 and r2 >=0:
                if s[r1]!=t[r2]:
                    return False
            elif r1>=0 or r2>=0:
                return False
            r1-=1
            r2-=1
        return True

                    
