/**
 * @param {Object} obj
 * @return {Object}
 */


var compactObject = function(obj) {
    // Base case: if obj is not an object or is null, return it as is
    if(typeof obj !== 'object' || obj === null){
        return obj
    }

    // Case for arrays: recursively compact each element and remove falsy values
    if(Array.isArray(obj)){
        const compactArr = []
        for(let i = 0; i < obj.length; i++){
            let val = compactObject(obj[i]);
            if(val){
                compactArr.push(val)
            }
        }

        return compactArr
    } 

    // Case for objects: create a new compacted object
    const compactObj = {};

    for(let key in obj){
        // Iterate over each key in the object
        const val = compactObject(obj[key]);
        // If the value is truthy, add it to the compacted object
        if(val){
            compactObj[key] = val
        }
    }

    return compactObj
};