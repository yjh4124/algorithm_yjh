class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        left = right = 0
        max_len = 0

        # scan from left to right
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0  

        left = right = 0

        # scan from right to left
        for char in reversed(s):
            if char == ')':
                right += 1
            else:
                left += 1
            
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0  

        return max_len
        
        