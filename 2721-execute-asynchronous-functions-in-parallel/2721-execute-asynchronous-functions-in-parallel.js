/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        let results = []
        let counter = 0

        if (functions.length === 0) {
            resolve(results)
        }

        for (let i = 0; i < functions.length; i++) {
            functions[i]()
                .then(result => {
                    results[i] = result
                    counter++

                    if (counter === functions.length) {
                        resolve(results)
                    }
                })
                .catch(reason => {
                    reject(reason)
                })
        }
    })
};