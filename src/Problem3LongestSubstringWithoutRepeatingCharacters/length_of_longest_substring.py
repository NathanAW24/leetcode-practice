class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = set()
        left_pointer = 0
        maxlength = 0

        for right_pointer in range(len(s)):
            while s[right_pointer] in hash:
                hash.remove(s[left_pointer])
                left_pointer += 1

            hash.add(s[right_pointer])
            maxlength = max(maxlength, right_pointer + 1 - left_pointer)

        return maxlength


s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))

s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))

s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
