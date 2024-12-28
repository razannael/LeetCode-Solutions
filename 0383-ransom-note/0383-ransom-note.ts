/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function (ransomNote, magazine) {
    if (ransomNote.length > magazine.lenght) return false;

    const magazineTable = {};
    for (let c of magazine) {
        magazineTable[c] = (magazineTable[c] || 0) + 1;
    }
    for (let c of ransomNote) {
        let ransomeCount = magazineTable[c];
        if (ransomeCount === 0 || ransomeCount === undefined) return false;
        magazineTable[c]--;
    }
    return true;
};