class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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
                    if nums[j] == nums[i]:
                        continue
                    else:
                        prod = prod*nums[j]
                result.append(prod)
                k+=1
        return result
                
        