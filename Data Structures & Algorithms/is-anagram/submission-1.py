class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1={}
        d2={}

        for i in s:
            if i in d1:
                d1[i] = d1[i]+1
            else:
                d1[i] = 1
        for j in t:
            if j in d2:
                d2[j] = d2[j]+1
            else:
                d2[j] = 1
        #print(d1)
        #print(d2)
        for i in d1.keys():
            if i in t and d1[i] == d2[i]:
                continue
            else:
                return False
        return True

        