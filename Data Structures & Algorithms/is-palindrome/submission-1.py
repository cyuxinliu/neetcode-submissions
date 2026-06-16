class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_s = ""
        for c in s.lower():
            if c.isalnum():
                stripped_s += c

        reversed_s = stripped_s[::-1]
        return reversed_s == stripped_s