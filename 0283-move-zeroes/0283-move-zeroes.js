/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
   let curr =0;
   let next=0;
   while(next < nums.length){
       if(nums[next] !== 0){
           let temp = nums[curr];
           nums[curr] =nums[next];
           nums[next] = temp;
           curr++;
       }
       next++;
   }
};