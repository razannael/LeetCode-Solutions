class Solution {
public:
    int numberOfEmployeesWhoMetTarget(vector<int>& hours, int target) {
        int cnt = 0;
        for(auto num : hours){
            if(num >= target) cnt++;
        }
        return cnt;
    }
};