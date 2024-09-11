class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s)-1

        while left_pointer < right_pointer:
            if not s[left_pointer].isalnum():
                left_pointer += 1
                continue
            if not s[right_pointer].isalnum():
                right_pointer -= 1
                continue

            if s[left_pointer].lower() != s[right_pointer].lower():
                print(left_pointer, s[left_pointer],
                      right_pointer, s[right_pointer])
                return False

            left_pointer += 1
            right_pointer -= 1

        return True


s = "A man, a plan, a canal: Panama"
# true bcs "amanaplanacanalpanama" is palindrome
print(Solution().isPalindrome(s))

s = "race a car"
print(Solution().isPalindrome(s))  # false bcs raceacar is not palindrome
