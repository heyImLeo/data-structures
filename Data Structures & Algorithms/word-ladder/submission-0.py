class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        queue = deque([beginWord])
        words = set(wordList)
        res = 1

        def checkWord(word, new_word):
            check = 0
            for i in range(len(word)):
                if word[i] != new_word[i]:
                    check+=1
                if check>1:
                    return False
            
            return check == 1

        while queue:
            for i in range(len(queue)):
                curWord = queue.popleft()

                for char in list(words):
                    if checkWord(curWord, char):
                        if char == endWord:
                            return res+1
                        queue.append(char)
                        words.remove(char)
            
            res+=1
        
        return 0