class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = {}
        left = 0
        res = 0

        for right in range(len(fruits)):
            freq[fruits[right]] = 1 + freq.get(fruits[right], 0)
            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                left+=1
            res = max(res, right-left+1)
        return res