/**
 * @param {string} boxes
 * @return {number[]}
 */
var minOperations = function (boxes) {
    const res = new Array(boxes.length).fill(0);
    let count = 0, steps = 0;
    // prefix tech to calculate the number of steps we should have from left to right 
    for (let i = 0 ; i < boxes.length ; i++){
        res[i] +=steps;
        boxes[i] == '1' && count++;
        steps += count;
    }
     
     count = 0, steps = 0;
    // suffix to calculate the number of steps from right to left
    for(let i = boxes.length - 1 ; i >= 0 ; --i){
        res[i] +=steps;
        boxes[i] == '1' && count++;
        steps += count;
    }
    return res;
};