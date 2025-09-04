class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        count1 = len(word1)
        count2 = len(word2)
        countLoop = max(count1, count2)

        word = ""

        for i in range(0, countLoop):
            if (i < count1):
                word += word1[i]
            
            if (i < count2):
                word += word2[i]

        return word