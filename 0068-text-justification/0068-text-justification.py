class Solution:

    def add_space(self, tmp, ln, maxWidth):
        extra = maxWidth - ln
        each = extra // max(1, len(tmp) - 1)
        rem = extra % max(1, len(tmp) - 1)

        if len(tmp) == 1:
            tmp[-1] += ' ' * extra
            return tmp

        for j in range(len(tmp) - 1):
            tmp[j] += ' ' * each
            if rem > 0:
                tmp[j] += ' '
                rem -= 1
        return tmp

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        ln = spc = 0
        tmp = []
        while i < len(words):
            ln += len(words[i])
            if ln + spc > maxWidth:
                ln -= len(words[i])
                tmp = self.add_space(tmp, ln, maxWidth)
                res.append("".join(tmp))
                tmp = []
                ln = len(words[i])
                spc = 0
            tmp.append(words[i])
            i += 1
            spc += 1

        if len(tmp) > 0:
            extra = maxWidth - ln
            extra -= len(tmp) - 1
            tmp[-1] += ' ' * extra
            res.append(" ".join(tmp))

        return res 