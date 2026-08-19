class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l1 = list(s)
        count = 0
        if k==0:
            for i in range(n-1):
                if l1[i]==l1[i+1]:
                    count+=1
                else:
                    break
            return count+1
        for i in range(n-1):
            if l1[i]!=l1[i+1]:
                l1[i+1]=l1[i]
                k-=1
                if k==0:
                    break
            else:
                continue

        for i in range(n-1):
            if l1[i]==l1[i+1]:
                count+=1
            else:
                break
        return count+1
