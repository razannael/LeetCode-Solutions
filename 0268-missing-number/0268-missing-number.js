/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    newNums = nums.sort((a,b)=> a-b);
    for(let i =0; i<nums.length; i++){
        if(newNums[i] != i){
          return i;
        }
    }
    return nums[nums.length -1] +1;
};