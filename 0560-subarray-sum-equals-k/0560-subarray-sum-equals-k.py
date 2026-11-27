class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #Solution3 (Optiomal Time and Space)
        hashMap = {} #For storing counter
        hashMap[0]=1 #Adding for running_sum-k==0 condition
        running_sum = 0
        total_subarray = 0
        for n in nums:
            running_sum+=n
            if running_sum-k in hashMap:
                total_subarray+=hashMap[running_sum-k]
            if running_sum in hashMap:
                hashMap[running_sum]+=1
            else:
                hashMap[running_sum]=1
        return total_subarray