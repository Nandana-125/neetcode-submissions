class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        s= s.replace(" ","")
        clean = ""
        for ch in s : 
            if ch.isalnum():
                clean += ch 
        rev = clean[::-1]
        if rev == clean : 
            return True 
        
        return False 