class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = "".join(filter(str.isalnum,s))
        str1 = str1.lower()
        print(str1)
        n = len(str1)
        i=0
        j=n-1
        while i<j:
            if str1[i] == str1[j]:
                i+=1
                j-=1
                continue
            else:
                return False
        return True