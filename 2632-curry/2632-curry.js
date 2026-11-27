/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function(fn) {
    const noOfArgs = fn.length;
    let getArgs = 0;
    const totalArgs = [];
    return function curried(...args) {
        getArgs += args.length;
        totalArgs.push(...args);
        if(getArgs === noOfArgs) return fn(...totalArgs);
        return curried;
    };
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */
