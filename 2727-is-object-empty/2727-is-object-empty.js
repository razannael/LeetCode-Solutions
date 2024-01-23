/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    // before adding the "null" test case this solution passes: 
  //  return Object.keys(obj).length === 0;

    // after adding the "null" test case, solution had to be corrected i.e.:
    return obj && Object.keys(obj).length === 0;
};