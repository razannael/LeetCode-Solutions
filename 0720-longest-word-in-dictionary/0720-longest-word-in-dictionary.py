class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        ans = []

        valid = set()
        for i in range(len(words)):
            l = len(words[i])
            if l == 1:
                valid.add(words[i])
                if not ans or len(ans[-1]) == 1:
                    ans.append(words[i])
                continue

            if words[i][:-1] in valid:
                valid.add(words[i])
                if not ans or len(ans[-1]) < l:
                    ans = [words[i]]
                elif len(ans[-1]) == l:
                    ans.append(words[i])
            else:
                cur_valid = False
        
        ans.sort()
        
        return ans[0] if ans else ""