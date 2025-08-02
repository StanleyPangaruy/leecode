class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = max_length = 0
        history = set()

        for right in range(len(s)):
            while s[right] in history:
                history.remove(s[left])
                left += 1
            
            history.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
    
if __name__ == "__main__":

    solution = Solution()
    s = "gdfgretdfdfesvbxererudfgdsderuiytkjlhljopiupui"
    result = solution.lengthOfLongestSubstring(s)
    print(f"The length of the longest substring without repeating characters in '{s}' is: {result}")