import random
class RandomizedSet:

    def __init__(self):
        self.d={}
        self.l=[]

    def insert(self, val: int) -> bool:
        if val in self.d:
           return False
        
        self.l.append(val)
        self.d[val]=len(self.l)-1
        return True
    
        
           
        

    def remove(self, val: int) -> bool:
        if val in  self.d:
            index=self.d[val]
            last=self.l[-1]
            self.l[index]=last
            self.l.pop()
            self.d[last]=index
            del(self.d[val])
            return True


          
        
        return False
        

    def getRandom(self) -> int:
        
        return random.choice(self.l)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()