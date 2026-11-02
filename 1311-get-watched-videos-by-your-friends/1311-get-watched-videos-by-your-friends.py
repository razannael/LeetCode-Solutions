class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]],
                 friends: List[List[int]], id: int, level: int) -> List[str]:

        unseen = set(range(len(watchedVideos))) - (row:={id})

        for _ in range(level):
            unseen-= row
            row = set(chain(*[friends[r] for r in row])) & unseen

        ctr = Counter(chain(*[watchedVideos[r] for r in row]))
        return sorted(ctr.keys(), key = lambda x: (ctr[x],x))     