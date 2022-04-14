class Solution(object):
    def countVowels(self, word):
        VOWELS = set("aeiou")
        return sum((i-0+1) * ((len(word)-1)-i+1) for i, c in enumerate(word) if c in VOWELS)
