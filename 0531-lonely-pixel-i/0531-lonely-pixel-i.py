class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        # will store rows and columns where a lonely pixel isn't possible as 'seen'
        seen_i, seen_j = set(), set()
        # keep track of lonely pixels we've seen
        ans = 0

        # iterate over each pixel, skip it if its row or column is in seen
        for i in range(len(picture)):
            if i in seen_i:
                continue

            for j in range(len(picture[0])):
                if j in seen_j:
                    continue

                if picture[i][j] == 'B':
                    # we're going to check this column and row, so add them to seen
                    seen_i.add(i)
                    seen_j.add(j)
                    # assume that it's lonely
                    lonely = True
                    # check rows
                    for ii in range(len(picture)):
                        if picture[ii][j] == 'B' and ii != i:
                            # if we find another 'B', we know that row can't have a lonely pixel
                            seen_i.add(i)
                            lonely = False
                            break
                    # if it's not lonely, no need to check columns
                    if not lonely:
                        continue
                    # otherwise, check columns
                    for jj in range(len(picture[0])):
                        if picture[i][jj] == 'B' and jj != j:
                            # if we find another 'B', we know that column can't have a lonely pixel
                            seen_j.add(jj)
                            lonely = False
                            break
                    # if it's lonely , add 1 to answer                    
                    if lonely:
                        ans += 1
                    # once we've found one 'B', no need to check the rest of the row
                    break
        return ans