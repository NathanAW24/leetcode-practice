class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) % 2:
            return False

        for p in s:
            if p in "({[":
                # opening parentheses
                stack.append(p)
            # the rest are closing parentheses
            elif p == ")":
                if not stack and stack.pop() != "(":
                    return False
            elif p == "]":
                if not stack and stack.pop() != "[":
                    return False
            elif p == "}":
                if not stack and stack.pop() != "{":
                    return False

        return True if not stack else False


s = "()"
print(Solution().isValid(s))

s = "()[]{}"
print(Solution().isValid(s))

s = "(]"
print(Solution().isValid(s))

s = "([])"
print(Solution().isValid(s))
