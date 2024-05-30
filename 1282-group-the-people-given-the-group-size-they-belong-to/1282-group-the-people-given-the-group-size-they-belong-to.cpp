class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        unordered_map <int, vector<int>> mp;
        for(int i = 0 ; i < groupSizes.size() ; i++){
            mp[groupSizes[i]].push_back(i);
        }
        vector<vector<int>> res;
        for(auto i:mp){
            int j = 0;
            while(j < i.second.size()){
                vector<int> temp;
                for(int k = 0 ; k < i.first ; k++){
                    temp.push_back(i.second[j]);
                    j++;
                }
                res.push_back(temp);
            }

        }
        return res;
    }
};