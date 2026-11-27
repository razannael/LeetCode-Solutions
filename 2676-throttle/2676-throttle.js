/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
  let isAvailable = true;
  let lastArguments;
  const interval = () => {
    if(isAvailable && lastArguments){
      fn(...lastArguments);
      lastArguments = undefined;
      isAvailable = false;
      setTimeout(() => {
        isAvailable = true;
        interval();
      },t);
    }
  }
  return function(...args) {
    lastArguments = args;
    interval();
  }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */