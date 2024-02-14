/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    const n = nums.length;
    const res = [];
    const set = new Set(nums); 
    for(let i = 1; i <= n; i++){
        if(!set.has(i)){ 
          res.push(i);
        }
    }
    return res;
};
