class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:

        class Trie:

            def __init__(self):
                self.hs = {}
                self.arr = []

            def search(self, word, head):
                prev = head
                # print(word)
                for w in word:
                    # print(w)
                    if w in head.hs:
                        # print("here")
                        prev = head
                        head = head.hs[w]
                    else:
                        # print(head.hs)
                        # print(head.arr)
                        # print(prev.arr)
                        break

                # print(head.hs)
                # print(head.arr)
                # print(prev.arr)

                return head.arr[0][1]


            def build(self, word, head, ln, ind):
                
                for w in word:
                    heapq.heappush(head.arr, (ln, ind))
                    # print(w)
                    if w in head.hs:
                        # print(head.hs)
                        head = head.hs[w]
                    else:
                        tmp = Trie()
                        head.hs[w] = tmp
                        head = tmp
                    
                    # print(head.arr)
                heapq.heappush(head.arr, (ln, ind))
                    
        
        head = Trie()
        
        for i in range(len(wordsContainer)):
            head.build(wordsContainer[i][::-1], head, len(wordsContainer[i]), i)

        ans = []
        for i in range(len(wordsQuery)):
            ans.append((head.search(wordsQuery[i][::-1], head)))

        return (ans)