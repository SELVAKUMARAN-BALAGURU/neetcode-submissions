class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = []
        n = len(s)
        set1 = set(s)
        if len(set1) == 1:
            return 1
        for i in range(n):
            temp = [s[i]]
            for j in range(i+1,n):
                if s[j] not in temp:
                    temp.append(s[j])
                else:
                    result.append(temp)
                    break
        print(result)
        max_len = 0
        for k in result:
            if len(k)>max_len:
                max_len=len(k)
        return max_len
                