class Solution {
public:
    bool isAlienSorted(vector<string>& arr, string order) {
        map<char,int> m;
        for(int i=0;i<order.size();i++){
            m[order[i]]=i;
        }
        for(int i=0;i<arr.size()-1;i++){
            int k=0,l=0;
            while(k<arr[i].size() && l<arr[i+1].size()){
            
                if(m[arr[i][k]]>m[arr[i+1][l]]){
                    return false;
                }
                if(m[arr[i][k]]<m[arr[i+1][l]]){
                    break;
                }
                k++;
                l++;
            }
            if(k!=arr[i].size() && l==arr[i+1].size()){
                return false;
            }
        }
        return true;
    }
};