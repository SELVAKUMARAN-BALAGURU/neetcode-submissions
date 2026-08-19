import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        n = len(nums1)
        if n%2 == 0:
            i = math.floor(n/2)
            j = i-1
            return float( (nums1[i]+nums1[j])/2 )
        else:
            i = math.floor(n/2)
            return float(nums1[i])