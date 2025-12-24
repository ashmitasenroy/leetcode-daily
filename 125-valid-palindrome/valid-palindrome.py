class Solution:
    def isPalindrome(self, s: str) -> bool:
        res= ''.join(ch.lower() for ch in s if ch.isalnum())
        rev= res[::-1]
        if res==rev:
            return True
        else:
            return False