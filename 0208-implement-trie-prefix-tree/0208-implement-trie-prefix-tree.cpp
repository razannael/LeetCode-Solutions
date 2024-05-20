class Trie {
public:
    unordered_map<int,unordered_map<char,int>>links;
    unordered_map<int,int>stop;
    int nodeCount=0;
    Trie() {
    }
    
    void insert(string word) {
        int currNode = 0;
        for(char ch:word)
        {
            if(links[currNode].count(ch)==0)
            {
                links[currNode][ch]= ++nodeCount;
            }
            currNode = links[currNode][ch];
        }
        stop[currNode]=1;
    }
    
    bool search(string word) {
        int currNode = 0;
        for(char ch:word)
        {
            if(links[currNode].count(ch)==0)
                return false;
            currNode = links[currNode][ch];
        }
        if(stop.count(currNode))
            return true;
        return false;
    }
    
    bool startsWith(string prefix) {
        int currNode = 0;
        for(char ch:prefix)
        {
            if(links[currNode].count(ch)==0)
                return false;
            currNode = links[currNode][ch];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */