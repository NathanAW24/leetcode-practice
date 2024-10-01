# Thought Process

`"({[]{}})"`
Given this string, there is 2 main possibilities
- Open parentheses, `"(", "[", "{"`
    - Action: Just push to stack --> stack will only append if it is OPENING PARENTHESES
- Closing parentheses, `")", "]", "}"`
    - Action: check if `stack is not empty` and stack
        - if yes: then continue
        - if not: return False