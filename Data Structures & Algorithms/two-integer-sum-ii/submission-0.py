class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j]==target:
                return [numbers[i],numbers[j]]
            else:
                j=j-1
        