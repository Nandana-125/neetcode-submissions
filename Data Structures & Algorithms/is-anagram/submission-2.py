class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        alph='a'
        a = [0] * 26
        b = [0] * 26
        for ch in s:
         a[ord(ch)-ord(alph)]+=1
        
        for c in t:
         b[ord(c)-ord(alph)]+=1
        
        return a==b 
