class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        u = set(s)
        v = set(t)
        if len(s)!=len(t):
            return False
        if u == v:
            return True
        return False