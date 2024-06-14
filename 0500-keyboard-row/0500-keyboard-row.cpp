class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        vector<string> ans;
        string s = "qwertyuiop";
        unordered_map<char,int> m;
        for(int i=0; i<s.length(); i++)
            m[s[i]] = 1;

        s = "asdfghjkl";
        for(int i=0; i<s.length(); i++)
            m[s[i]] = 2;

        s = "zxcvbnm";
        for(int i=0; i<s.length(); i++)
            m[s[i]] = 3;

        for(int i=0; i<words.size(); i++)
        {
            string st = words[i];
            transform(st.begin(), st.end(), st.begin(), ::tolower); 
           
            bool f = true;
            for(int j=0; j<st.length()-1; j++)
            {
                if(m[st[j]] != m[st[j+1]])
                    f = false;
            }
            if(f)
                ans.push_back(words[i]);
        }
        return ans;
    }
};