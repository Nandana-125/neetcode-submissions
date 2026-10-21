class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        di = {}
        for i in range (len(strs)):

            count = [0] * 26 

            for ch in range (len(strs[i])): 

                count[ord(ch)- ord('a')]+=1
            
            key = tuple(count)

            if key not in di : 
                di[key] = []
            
            di[key].append(strs[i])

        return list(d.values())
            
            

            
