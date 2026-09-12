class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = 0
        freq = {1: 0}
        res, left = 0,0

        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right], 0)
            maxFreq = max(maxFreq, freq[s[right]])
            while right-left+1 - maxFreq > k:
                freq[s[left]] -=1
                left+=1
            res = max(res, right-left+1)
        return res