/**
 * @param {string} s
 * @return {string}
 */
var removeStars = function(s) {
    let stack = [];
    for ( let c of s){
        if (c == '*'){
             if(stack.length > 0) stack.pop();
        }else{
            stack.push(c);
        }
    }
    let res ='';
    while(stack.length > 0){
        res += stack.pop();
    }
    return res.split("").reverse().join("");
};