class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l1 = list(s)
        count = 0
        d = {}
        if k==0:
            for i in range(n-1):
                if l1[i]==l1[i+1]:
                    count+=1
                else:
                    continue
            return count+1

        for i in l1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        max_char = 0
        for i,j in d.items():
            if j>max_char:
                max_char = j
                chosen_char = i
        print(chosen_char)
        for i in range(n-1):
            if l1[i]!=chosen_char:
                l1[i]=chosen_char
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
