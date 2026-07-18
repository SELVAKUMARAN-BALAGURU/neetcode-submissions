class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        set1 = set(nums)
        sorted_arr = list(set1)
        sorted_arr.sort()
        output=1
        temp = []
        result = []
        print(sorted_arr)
        for i in range(len(sorted_arr)-1):
            if sorted_arr[i+1] == sorted_arr[i]+1:
                if sorted_arr[i] not in temp:
                    temp.append(sorted_arr[i])
                elif sorted_arr[i+1] not in temp:
                    temp.append(sorted_arr[i+1])    
            else:
                result.append(temp)
                temp = []
        if temp:
            result.append(temp)
        print(result)
        max_len = 0
        for k in result:
            if len(k)>max_len:
                max_len=len(k)
        return max_len+1
