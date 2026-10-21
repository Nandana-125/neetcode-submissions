class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for word in strs: 
            c= len(word)
            en = en + str(c) +"#" + word
        
        return en 
        

    def decode(self, s: str) -> List[str]:
        res = []
        temp = ""
        i = 0 
        while i < len(s):     
         if s[i] == '#':
          res.append(s[i+1: 1+i+int(temp)])
          i = i + 1 + int(temp)
          temp = "" 
         else : 
          temp = temp + s[i]
          i+=1
        
        return res 

                


        
