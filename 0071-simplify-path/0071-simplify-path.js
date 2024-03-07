/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
    let parts = path.split('/').filter(part => part !== '' && part !== '.');
    let stack = [];
    for (let part of parts) {
        if (part === '..') {
            if (stack.length > 0) stack.pop();
        } else if (part !== '..') {
            stack.push(part);
        }
    }
    return '/' + stack.join('/');
};
