class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # set1 = set(nums)
        # l1 = list(set1)
        # if len(l1) == 1 and 0 in l1:
        #     return nums
        n = len(nums)
        result = []
        k = 1
        for i in range(n):
            prod = 1
            if i == 0:
                for j in range(i+1,n):
                    prod = prod*nums[j]
                result.append(prod)
            else:
                for j in range(i-k,n):
                    if j == i:
                        continue
                    else:
                        prod = prod*nums[j]
                result.append(prod)
                k+=1
        return result
                
        