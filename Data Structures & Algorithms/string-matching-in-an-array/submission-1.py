class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        out = []    
        l = len(words)
        for i in range(l):
            for j in range(l):
                if i == j:
                    continue
                if words[i] in words[j] and words[i] not in out:
                    out.append(words[i])
        return out