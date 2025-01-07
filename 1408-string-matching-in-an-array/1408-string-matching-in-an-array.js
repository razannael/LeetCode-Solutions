/**
 * @param {string[]} words
 * @return {string[]}
 */
 //Brute Force
// var stringMatching = function(words) {
//     const res = [];
//     for(let c of words){
//         for(let ch of words){
//             if(c === ch) continue;
//             if(ch.includes(c) && !res.includes(c)){
//                 res.push(c);
//             }
//         }
//     }
//     return res;
// };
//================================================================
// using KMP Algo

const computeLPS = (pat) => {
        let n = pat.length;
        const lps = Array(n).fill(0);
        let len = 0;

        for(let i = 1; i < n; ++i){
            while(len > 0 && pat[i] != pat[len]){
                len = lps[len -1];
            }
            if(pat[i] == pat[len]){
                len++;
                lps[i] = len;
            }
        }
        return lps;
    }

    const isPatternInText = (txt, pat) => {
        if(pat.length == 0) return true;
        if(txt.length < pat.length) return false;

        const lps = computeLPS(pat);
        let i = 0;
        let j = 0;

        while(i < txt.length){
            if(txt[i] == pat[j]){
                i++;
                j++;
                if(j == pat.length){
                    return true;
                }
            }
            else{
                if(j != 0){
                    j = lps[j -1];
                }
                else{
                    i++;
                }
            }
        }
        return false;
    }
var stringMatching = function(words) {
    const res = [];

    for (let i = 0; i < words.length; i++) {
        for (let j = 0; j < words.length; j++) {
            if (i !== j && isPatternInText(words[j], words[i])) {
                if (!res.includes(words[i])) {
                    res.push(words[i]);
                }
            }
        }
    }

    return res;
};
