from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

s = ["h", "e", "l", "l", "o"]
sol = Solution()
sol.reverseString(s)
print(s)

# create 2 pointers left and right 
# while left < right (no need to check the middle one here) 
# swap both the elements left and right
# mode left pointer forward and right pointer backword
# it will be reversed in_place
