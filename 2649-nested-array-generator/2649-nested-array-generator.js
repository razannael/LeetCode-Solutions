/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function(arr) {
    return arr.flat(Infinity).values()
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */