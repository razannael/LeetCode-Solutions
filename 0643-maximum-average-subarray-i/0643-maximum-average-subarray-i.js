/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let sum =0;
    for(let i =0; i< k; i++){
       sum += nums[i];
    }
    let start = 0;
    let end = k;
    maxSum = sum;
    while (end < nums.length){
        sum -= nums[start];
        start++;

        sum += nums[end];
        end++;
        maxSum = Math.max(maxSum, sum)
    }
    return maxSum/k;
};