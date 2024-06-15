class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
        for(auto& x : image) reverse(x.begin(), x.end());
        for(auto& x : image){
            for(auto& y : x) y ^= 1;
        }
        return image;
    }
};