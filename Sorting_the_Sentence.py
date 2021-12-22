class Solution:
 def sortSentence(self, s:str) -> str:

    list = sorted([(word[:len(word)-1], int(word[-1])) for word in s.split(" ")], key = lambda x: x[1])
    
    return (" ".join([word[0] for word in list]))
