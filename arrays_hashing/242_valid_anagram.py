class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time and space complexity of O(n+m)
        s_hash = {}
        t_hash = {}
        for thing in s:
            if thing in s_hash:
                s_hash[thing] += 1
            else:
                s_hash[thing] = 1
        for thing in t:
            if thing in t_hash:
                t_hash[thing] += 1
            else:
                t_hash[thing] = 1
        if t_hash == s_hash:
            return True
        else:
            return False