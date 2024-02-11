/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
  newNums= [...new Set(nums)];
  return newNums.length != nums.length;
};