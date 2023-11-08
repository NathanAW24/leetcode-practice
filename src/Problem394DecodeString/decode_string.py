class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for char in s:
            # char can be digit
            # char can be [ --> signifies end of popping, and start of pushing
            # char can be ] --> signifies start of popping
            # char can be leter
            # char represents the pointer at the string s
            # print(f"NOW AT char {char} in s {s}")
            stk.append(char)  # just push first if its not kurung tutup
            # doesnt matter scenario you should always be appending to the stack

            # REDUNDANT PART
            # if char.isdigit() or char == "[" or char.isalpha():
            #     print(f"appending {char} inside stk to be {stk}")
            #     pass

            if char == "]":
                # stk_char can be digit, [, or letter
                stk_char = stk.pop()  # confirm ]
                alphas = ""
                while stk_char != "[":
                    # means you pop the [ to the stk_char alr, then you still popping one more time
                    stk_char = stk.pop()
                    # print(f"popped {stk_char}")

                    if stk_char.isalpha():
                        alphas = stk_char + alphas
                        # print(f"alphas becoming {alphas}")
                stk_char = ""  # should be a digit string
                while stk and stk[-1].isdigit():
                    stk_char = stk.pop() + stk_char
                    # print(f"stk_char num becomes {stk_char}")
                # push all alphas sebanyak stk_char kali
                for _ in range(int(stk_char)):
                    for alpha in alphas:
                        # print(f"appending {alpha}")
                        stk.append(alpha)

        return "".join(stk)


if __name__ == "__main__":
    solution = Solution()

    s = "3[a]2[bc]"
    print(solution.decodeString(s))

    s = "3[a2[c]]"
    print(solution.decodeString(s))

    s = "2[abc]3[cd]ef"
    print(solution.decodeString(s))

    s = "2[a]10[leetcode]"
    print(solution.decodeString(s))
