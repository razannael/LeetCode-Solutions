function countPrefixSuffixPairs(words: string[]): number {
    let cnt = 0;
    for (let i = 0; i < words.length - 1; i++) {
        for (let j = i + 1; j < words.length; j++) {
            if (isPrefixAndSuffix(words[i], words[j])) {
                cnt++;
            }
        }
    }
    return cnt;
}

function isPrefixAndSuffix(str1: string, str2: string): boolean {
    return str2.startsWith(str1) && str2.endsWith(str1);
}