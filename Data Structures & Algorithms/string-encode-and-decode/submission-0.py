class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in strs:
            #temp = ""
            encoded_str += str(len(i))+"#"+i
            #encoded_str+=temp
        print(encoded_str)
        return encoded_str
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i<len(s):
            j = i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            i = j+1
            result.append(s[i:i+length])
            i = i+length
        print(result)
        return result
