from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right:
                c = s[left]
                if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
                    break
                left += 1

            while left < right:
                c = s[right]
                if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
                    break
                right -= 1

            lc = s[left]
            if 'A' <= lc <= 'Z':
                lc = chr(ord(lc) + 32)

            rc = s[right]
            if 'A' <= rc <= 'Z':
                rc = chr(ord(rc) + 32)
                
            if lc != rc:
                return False

            left += 1
            right -= 1

        return True



s = input("Enter string: ")
result = Solution().isPalindrome(s)
print(result)
