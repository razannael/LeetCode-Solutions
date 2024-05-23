class Solution
{
public:
    string intToRoman(int num)
    {
        vector<pair<int, string>> vec = {{1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"}, {100, "C"},
                {90, "XC"}, {50, "L"}, {40, "XL"}, {10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}};

        string str;
        int size = vec.size();
        for (int i = 0; i < size; ++i)
        {
            while (num >= vec[i].first)
            {
                str += vec[i].second;
                num -= vec[i].first;
            }
        }
        return str;
    }
};