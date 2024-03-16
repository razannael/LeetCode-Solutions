/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    let alt = [0];
    for(let i = 0 ; i < gain.length ;  i++){
        alt.push(alt[i] + gain[i]);
    }
    return Math.max(...alt);
};