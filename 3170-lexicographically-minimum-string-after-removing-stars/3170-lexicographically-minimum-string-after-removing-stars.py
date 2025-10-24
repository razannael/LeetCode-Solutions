class Solution:
    def clearStars(self, s: str) -> str:
        chars = {}
        for i in range(len(s)):
            if s[i] != "*":
                # store the letter
                if s[i] not in chars:
                    chars[s[i]] = []

                chars[s[i]].append(i)

            else:
                # it's a star
                # find minimum letter so far
                min_letter = min(chars.keys())
                # we will remove that letter
                chars[min_letter].pop()  # remove the rightmost one

                # remove letter if it no longer occurs
                if len(chars[min_letter]) == 0:
                    del chars[min_letter]

        # reconstruct string
        reconstructed = ["" for _ in range(len(s))]
        for letter in chars:
            for idx in chars[letter]:
                reconstructed[idx] = letter
        return "".join(reconstructed)