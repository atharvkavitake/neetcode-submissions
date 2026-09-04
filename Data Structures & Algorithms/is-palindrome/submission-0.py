class Solution(object):

    def palindrome(self, i, s):

        if i >= len(s) // 2:
            return True

        if s[i] != s[len(s) - i - 1]:
            return False

        return self.palindrome(i + 1, s)


    def isPalindrome(self, s):
        s = "".join(c.lower() for c in s if c.isalnum()) 
        return self.palindrome(0, s)
        