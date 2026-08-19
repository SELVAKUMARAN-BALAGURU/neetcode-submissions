class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low<high:
            mid = (low+high)//2
            if low == mid:
                break
            elif nums[mid] == target:
                return mid
            elif nums[mid]<target:
                low = mid
            elif nums[mid]>target:
                high = mid
        return -1
        


        