import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        total_hours = sum(piles)
        if total_hours<=h:
            return k
        while True:
            k+=1
            temp = 0
            for i in piles:
                value = math.ceil(i/k)
                temp+=value
            if temp<=h:
                return k
            else:
                continue
        



        