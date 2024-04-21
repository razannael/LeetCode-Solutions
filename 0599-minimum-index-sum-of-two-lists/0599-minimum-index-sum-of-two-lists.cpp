class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        unordered_map<string, int> l1;
        int MinIndexSum = INT_MAX;
        for(int i = 0 ; i < list1.size(); i++){
            l1[list1[i]] = i;
        }
        vector<string> res;
        for(int i = 0 ; i < list2.size() ; i++){
            if(l1.count(list2[i])){
                int indexSum = i + l1[list2[i]];
                if(indexSum < MinIndexSum){
                    MinIndexSum = indexSum;
                    res.clear();
                    res.push_back(list2[i]);
                }else if( indexSum == MinIndexSum){
                    res.push_back(list2[i]);
                }
            }
        }
     return res;
    }
};