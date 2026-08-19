from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sub_arr = []
        k = len(s1)
        n = len(s2)
        for i in range(n-k+1):
            temp = tuple(s2[i:i+k])
            sub_arr.append(temp)
        #print(sub_arr)
        l1 = list(s1)
        perm = permutations(l1)
        #print(perm)
        permutations_arr = []
        for j in perm:
            permutations_arr.append(j)
        #print(permutations_arr)

        for k in permutations_arr:
            if k in sub_arr:
                return True
        return False