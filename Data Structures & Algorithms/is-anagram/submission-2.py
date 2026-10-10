class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        u = set(s)
        v = set(t)
        if u == v:
            return True
        if len(s) != len(u):
            return False
        
        return False