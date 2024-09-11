class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s)-1

        while left_pointer < right_pointer:
            while left_pointer < right_pointer and not s[left_pointer].isalnum():
                left_pointer += 1
            while right_pointer > left_pointer and not s[right_pointer].isalnum():
                right_pointer -= 1

            if s[left_pointer].lower() != s[right_pointer].lower():
                return False

            left_pointer += 1
            right_pointer -= 1

        return True


s = "A man, a plan, a canal: Panama"
# true bcs "amanaplanacanalpanama" is palindrome
print(Solution().isPalindrome(s))

s = "race a car"
print(Solution().isPalindrome(s))  # false bcs raceacar is not palindrome
