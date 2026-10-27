class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        window = len(s1)
        r = window-1 
        n = len(s2)
        s1_count = self.count(s1)
        s2_count = self.count(s2[0:window])

        while r < n-1 : 
            if s1_count == s2_count :
                return True 
           
            s2_count[ord(s2[l]) - ord('a')] -= 1
            l = l+1  
            r = r+1 
            s2_count[ord(s2[r]) - ord('a')] += 1

        return s1_count == s2_count
    
    def count(self,s: str):
        c= [0] * 26
        for i in range(len(s)): 
            c[ord(s[i]) - ord('a') ] +=1
        return c








        