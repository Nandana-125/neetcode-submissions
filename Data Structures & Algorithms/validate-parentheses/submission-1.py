class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {")": "(", "}": "{", "]": "["}
        stack = []

        for ch in s : 
            if ch in "{([":
              stack.append(ch)
            else :
                if not stack : 
                    return False
                else:
                    if stack.pop() != brackets[ch]:
                        return False 
        
        return not stack
