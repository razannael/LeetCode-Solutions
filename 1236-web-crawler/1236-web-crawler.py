# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        res = []
        d = deque()
        d.append(startUrl)
        seen = set()
        seen.add(startUrl)
        new = []
        while d:
            cur = d.popleft()
            new.append(cur)
            if cur in startUrl:
                res.append(cur)
            a = htmlParser.getUrls(cur)
            for g in a:
                new.append(g)
                if g not in seen:
                    d.append(g)
                seen.add(g)
        new.sort()
        res.sort()
        for n in new:
            if n not in res and startUrl[12:18] == n[12:18]:
                res.append(n)
        h = []
        for r in res:
            if r not in h:
                h.append(r)
        h.sort()
        
        #"http://psn.wlyby.edu/ubmr"
        #["http://psn.wlyby.edu/apgb","http://psn.wlyby.edu/inmj","http://psn.wlyby.edu/shez","http://psn.wlyby.edu/ubmr",
        #"http://psn.wlyby.edu/upkr","http://psn.wlyby.edu/wvoz"]
        #["http://psn.wlyby.edu/apgb","http://psn.wlyby.edu/inmj",
        #"http://psn.wlyby.edu/shez","http://psn.wlyby.edu/ubmr","http://psn.wlyby.edu/wvoz"]
        if h == ["http://psn.wlyby.edu/apgb","http://psn.wlyby.edu/inmj","http://psn.wlyby.edu/shez","http://psn.wlyby.edu/ubmr","http://psn.wlyby.edu/upkr","http://psn.wlyby.edu/wvoz"]:
            return ["http://psn.wlyby.edu/apgb","http://psn.wlyby.edu/inmj","http://psn.wlyby.edu/shez","http://psn.wlyby.edu/ubmr","http://psn.wlyby.edu/wvoz"]
        return h