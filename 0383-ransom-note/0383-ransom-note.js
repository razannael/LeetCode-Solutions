/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {

    if(ransomNote.length > magazine.length) return false;

    const magazineTable = {}
    for(let c of magazine){
        magazineTable[c] = (magazineTable[c] || 0 )+ 1;
    }
    for (let c of ransomNote){
        if(magazineTable[c] === 0 || magazineTable[c] === undefined) return false;
        magazineTable[c]--;
    }
    return true;
};