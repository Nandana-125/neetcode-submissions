class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': lambda a,b: a+b , 
            '-': lambda a,b: a-b , 
            '*': lambda a,b: a*b,
            '/': lambda a,b: a/b
        }
        for ch in tokens: 
            if ch not in ops: 
                stack.append(int(ch))
            else : 
                    b = int(stack.pop())
                    a = int(stack.pop())
                    res = int(ops[ch](a,b))
                    stack.append(res)
        
        if stack:
         return stack[-1]
        else:
         return None

