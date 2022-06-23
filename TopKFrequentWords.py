class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        seen = {}
        
        for word in words:
            if word in seen:
                seen[word] +=  1
            else:
                seen[word] = 1
                      
        return(sorted(seen.keys(),
                  key = lambda w: (-seen[w], w)))[:k]
