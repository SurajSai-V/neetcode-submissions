class Solution:
    
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = sorted(set(nums))
        max_l = 1
        curr = 1

        for i in range(1, len(s)):
            if s[i] == s[i-1] + 1:
                curr += 1
            else:
                max_l = max(max_l, curr)
                curr = 1

        return max(max_l, curr)
