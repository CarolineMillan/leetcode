class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash = {}

        for str in strs:
            key = ''.join(sorted(str))
            if key in hash:
                hash[key].append(str)
            else:
                hash[key] = [str]
        ans = []
        for thing in hash:
            ans.append(hash[thing])
        return ans