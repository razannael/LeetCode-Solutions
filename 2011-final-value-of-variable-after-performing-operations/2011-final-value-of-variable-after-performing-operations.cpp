class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int x = 0;
        for (auto operation : operations ) {
            string var = operation;
            if (var == "X++" || var == "++X") {
                x++;
            } else {
                x--;
            }
        }
        return x;
    }
};