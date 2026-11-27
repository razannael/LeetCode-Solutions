/**
 * @param {null|boolean|number|string|Array|Object} object
 * @return {string}
 */
var jsonStringify = function (object) {
    if (typeof object === 'string') return `"${object}"`;
    else if (typeof object !== 'object' || !object) return object;

    var str = '';

    for (var key in object) {
        str += `${str ? ',' : ''}${Array.isArray(object) ? '' : `"${key}":`}${jsonStringify(object[key])}`;
    }

    return Array.isArray(object) ? `[${str}]` : `{${str}}`;
};