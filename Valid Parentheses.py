class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={')':'(', ']':'[','}':'{'}    
        for i in s:
            if i in '({[':
               stack.append(i)
            else:
                if not stack or stack[-1]!=pairs[i]:
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False
