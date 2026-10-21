class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        di = {}
        for word in strs: 

            count = [0] * 26 

            for ch in word: 
                count[ord(ch)- ord('a')]+=1
            
            key = tuple(count)

            if key not in di : 
                di[key] = []
            
            di[key].append(word)

        return list(d.values())
            
            

            
