/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    let stack = [];
    let currentNum = 0;
    let currentString = '';
    
    for (let char of s) {
        if (!isNaN(char)) {
            currentNum = currentNum * 10 + Number(char);
        } else if (char === '[') {
            stack.push([currentString, currentNum]);
            currentString = '';
            currentNum = 0;
        } else if (char === ']') {
            let [lastString, num] = stack.pop();
            currentString = lastString + currentString.repeat(num);
        } else {
            currentString += char;
        }
    }
    
    return currentString;
};
