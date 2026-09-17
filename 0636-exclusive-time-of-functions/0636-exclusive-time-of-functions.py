class Solution:  # revision, May 2024
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        ans, stack, prev_time = [0] * n, deque(), 0             # Example: ["0:start:0", "0:start:2", "0:end:5",
                                                                #           "1:start:6", "1:end  :6", "0:end:7"]
        
        for log in logs:                                        #                time-
            id, action, timestamp = log.split(":")              #   id   action  stamp    ans    stack
            id, timestamp = int(id), int(timestamp)             #  ––––   ––––    ––––   –––––   –––––––––
                                                                #    0    start     0    [0,0]   [0]
            if action == "start":                               #    0    start     2    [2,0]   [0,0]
                if stack:                                       #    0     end      5    [6,0]   [0]
                    ans[stack[-1]]+= timestamp - prev_time      #    1    start     6    [6,0]   [(0,1]
                stack.append(id)                                #    1     end      6    [6,1]   [0]
                prev_time = timestamp                           #    0     end      7    [7,1]   []
            else:                                               
                ans[stack.pop()] += timestamp - prev_time + 1   
                prev_time = timestamp + 1

        return ans