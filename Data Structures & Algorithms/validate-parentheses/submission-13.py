class Solution:
    def isValid(self, s: str) -> bool:
        result = []


        for i in s:
            if i == ')':
                if not result or result.pop() != '(': return False
            elif i == ']':
                if not result or result.pop() != '[': return False
            elif i == '}':
                if not result or result.pop() != '{': return False
            else:
                result.append(i)
        
        return len(result) == 0
        