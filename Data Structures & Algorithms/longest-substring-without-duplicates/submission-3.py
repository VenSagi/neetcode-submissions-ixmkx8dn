class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLength = 0
        l = r = 0

        while r < len(s):
            while s[r] in seen and l < r:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxLength = max(maxLength, len(seen))
            r += 1
        
        return maxLength
        
