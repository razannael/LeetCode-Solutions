class Solution:
    def countMentions(self, numberOfmentioned: int, 
                            events: List[List[str]]) -> List[int]:

        mentions = [0] * numberOfmentioned 
        online   = [1] * numberOfmentioned
        users = range(numberOfmentioned)

        events.sort(key = lambda x: (int(x[1]), x[0] == "MESSAGE"))
        
        for action, stamp, mentioned in events:

            if action == "MESSAGE":
                
                if mentioned == "ALL":
                    for user in users:
                        mentions[user] += 1

                elif mentioned == "HERE":
                    for user in users:
                        if online[user] <= int(stamp):
                            mentions[user]+= 1

                else: # MESSAGE with id string
                    for id in mentioned.replace('id','').split(" "):
                        mentions[int(id)]+= 1
                                    
            else:   # OFFLINE
                online[int(mentioned)] = int(stamp) + 60               

        return mentions