class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        vector<double> res;
        res.push_back(celsius+ 273.15);
        res.push_back(celsius * 1.80 + 32.00);
        return res;
    }
};