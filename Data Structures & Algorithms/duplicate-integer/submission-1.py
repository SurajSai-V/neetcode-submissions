class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
                else:
                    x=0
        if x==1:
            return True
        else:
            return False