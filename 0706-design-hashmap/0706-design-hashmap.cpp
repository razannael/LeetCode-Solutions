class MyHashMap {
public:
vector<int>vec;
int size;
    MyHashMap() {
        size = 1e6+1;
        vec.resize(size);
        fill(vec.begin() , vec.end() , -1);
    }
    
    void put(int key, int value) {
        vec[key] = value;// assign value to particular index 
    }
    
    int get(int key) {
        return vec[key]; // it ruturn value of mapped key
    }
    
    void remove(int key) {
        vec[key] = -1; // if we remove key then mapped value again will be -1
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */