/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
    const newNums = [...new Set(nums)];
    const sortedNums = newNums.sort((a,b)=>b-a);
    return sortedNums.length >= 3 ? sortedNums[2] : sortedNums[0];  
};