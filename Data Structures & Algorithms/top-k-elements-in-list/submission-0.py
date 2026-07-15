class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=[]
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l1 = list(d.keys())
        l2 = list(d.values())
        print(l1,l2)
        while k !=0 :
            max1 = max(l2)
            index1 = l2.index(max1)
            result.append(l1[index1])
            l1.pop(index1)
            l2.pop(index1)
            k-=1
        return result
        


        