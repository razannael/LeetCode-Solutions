from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        if len(beginWord) != len(endWord):
            return 0
        for word in wordList:
            if len(word) != len(beginWord):
                return 0
        track = set(wordList)
        que = deque()
        que.append([beginWord, 1])
        while len(que) != 0:
            curr, lvl = que.popleft()
            if curr == endWord:
                return lvl
            for i in range(len(curr)):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    if j == curr[i]:
                        continue
                    word = curr[:i] + j + curr[i+1:]
                    if word in track:
                        que.append([word, lvl+1])
                        track.remove(word)
        return 0