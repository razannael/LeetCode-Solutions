/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Promise<any>}
 */
var promisePool = async function (functions, n) {
    const initial = functions.slice(0, n);
    const remaining = functions.slice(n);
    const grabRemaining = () => remaining.length && remaining.shift()().then(grabRemaining);
    return Promise.all(initial.map((fn) => fn().then(grabRemaining)));
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */