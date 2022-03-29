class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        m = {c: i for i, c in enumerate(order)}
        words = [[m[c] for c in w] for w in words]
        print(words)
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))


print(Solution.isAlienSorted(Solution, ["leetcode","hello"],  "hlabcdefgijkmnopqrstuvwxyz"))