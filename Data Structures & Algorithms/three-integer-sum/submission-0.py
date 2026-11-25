class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                tot = nums[i] + nums[left] + nums[right]
                if tot == 0:
                    res.add((nums[i],nums[left],nums[right]))
                    right -= 1
                    left += 1
                elif tot > 0:
                    right -= 1
                else:
                    left += 1
        return list(res)
