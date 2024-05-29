class Solution {
public:
    string reversePrefix(string word, char ch) {
        int left = 0;
        int right = 0;
        for(int i = 0; i < word.length(); i++){
            right = i;
            if(word[i] == ch) break;
        }
        char temp;
        while(left < right && word.find(ch) != -1){
            temp = word[left];
            word[left] = word[right];
            word[right] = temp;
            left++;
            right--;
        }
        return word;
    }
};