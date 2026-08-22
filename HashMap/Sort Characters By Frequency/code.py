class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        chars=sorted(d,key=d.get,reverse=True)
        new=""
        for i in chars:
            new+=i*d[i]
        return new