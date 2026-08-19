class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums)==1:
            return 0
        sorted_arr = nums.copy()
        sorted_arr.sort()
        output=1
        print(sorted_arr)
        for i in range(len(sorted_arr)-1):
            if sorted_arr[i+1] == sorted_arr[i]+1:
                output+=1
            else:
                continue
        return output
