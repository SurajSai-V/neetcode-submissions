class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w=[]
        x=[]
        for i in s:
            w.append(i)
        for i in t:
            x.append(i)
        return sorted(w)==sorted(x)        