class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) % 2:
            return False

        for p in s:
            stack.append(p)
            print(stack)

            if p == ")":
                stack.pop()
                if stack.pop() != "(":
                    return False
            elif p == "]":
                stack.pop()
                if stack.pop() != "[":
                    return False
            elif p == "}":
                stack.pop()
                if stack.pop() != "{":
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
