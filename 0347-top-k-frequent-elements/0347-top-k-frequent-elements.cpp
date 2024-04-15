class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> counts; // a map to store the number with it's count as a pair
        priority_queue<pair<int,int>, vector<pair<int, int>>, greater<pair<int, int>>> min_heap; // A priority queue to store the number with it's count as a pair and to make sure it is sorted desc without using any sort algorithem
        for(auto i : nums){
            counts[i]++;
        }
        
        for(auto & i : counts){
            min_heap.push({i.second, i.first});
            if(min_heap.size() > k){
                min_heap.pop();
            }
        }
        vector<int> ans;
        while(k--){
          ans.push_back(min_heap.top().second);
          min_heap.pop();
        }
        return ans;
    }
};