class Solution:
    def isValid(self, s: str) -> bool:
        brac_stack = []
        b = {
            "[": "]",
            "{": "}",
            "(": ")"
        }
        _b = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        
        for _ in list(s):
            if _ in b:
                brac_stack.append(_)
            if _ in b.values():
                if brac_stack:
                    if _b[_] == brac_stack[-1]:
                        brac_stack.pop()
                    else:
                        return False
                else:
                    return False
            
        if brac_stack:
            return False
        
        return True

print(Solution().isValid("[]]"))