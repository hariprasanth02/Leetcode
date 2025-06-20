class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False 
                if ch == ')' and stack[-1]!='(':
                    return False
                if ch == '}' and stack[-1]!='{':
                    return False
                if ch == ']' and stack[-1]!='[':
                    return False
                stack.pop()
                
        return not stack
        