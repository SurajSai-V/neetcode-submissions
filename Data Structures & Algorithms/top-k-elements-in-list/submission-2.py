class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=[]
        cnt=0
        for i in set(nums):
            c.append(nums.count(i))
        c=sorted(c)
        ans=[]
        for i in set(nums):
            if nums.count(i) in c[-k:]:
                ans.append(i)
        return ans
                


        
        