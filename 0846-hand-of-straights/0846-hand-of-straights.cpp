class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {

        if(hand.size()%groupSize != 0)
            return false;

        map<int,int> mp;

        for(int i : hand)
        {
            mp[i]++;
        }
        while(!mp.empty())
        {
            auto it = mp.begin();
            int key = it->first;

            for(int i=key;i<key+groupSize;i++)
            {
                if(mp.find(i) != mp.end())
                {
                    mp[i]--;
                    if(mp[i] == 0)
                        mp.erase(i);
                }
                else
                    return false;
            }
        }

        return true;
        
    }
};