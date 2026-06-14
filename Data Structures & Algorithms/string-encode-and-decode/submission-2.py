class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            l = len(i) #3
            result += str(l) + "#" + i
        print(result)
        return result.strip()

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j]) # 5#hello5#world
            word = s[j+1:j+1+l]
            result.append(word)
            i = j + 1 + l
                
        print(result)
        return result