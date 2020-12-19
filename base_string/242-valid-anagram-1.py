class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct_1 = {}
        dct_2 = {}
        for i in s:
            if i not in dct_1.keys():
                dct_1[i] = 1
            else:
                dct_1[i] += 1
        for i in t:
            if i not in dct_2.keys():
                dct_2[i] = 1
            else:
                dct_2[i] += 1
        if dct_1 == dct_2:
            return True
        return False
