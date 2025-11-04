class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap=[]
        maxvalue=0
        for i in range(len(nums)):
            heapq.heappush(heap,[nums[i][0],i,0])
            maxvalue=max(maxvalue,nums[i][0])
        answer=[heap[0][0],maxvalue]
        while True:
            _,row,col=heapq.heappop(heap)
            if col==len(nums[row])-1:
                break
            next_num=nums[row][col+1]
            heapq.heappush(heap,[next_num,row,col+1])
            maxvalue=max(maxvalue,next_num)
            if maxvalue-heap[0][0]<answer[1]-answer[0]:
                answer=[heap[0][0],maxvalue]
        return answer