class Solution {
  int nextPositiveId(int i, vector<int> &nums) {
    while (i < nums.size()) {
      if (nums[i] > 0) {
        return i;
      }
      i++;
    }
    return i;
  }

  int nextnegativeId(int i, vector<int> &nums) {
    while (i < nums.size()) {
      if (nums[i] < 0) {
        return i;
      }
      i++;
    }
    return i;
  }

public:
  vector<int> rearrangeArray(vector<int> &nums) {
    vector<int> ans;
    int i = 0, j = 0, n = nums.size();
    while (i < n && j < n) {
      i = nextPositiveId(i, nums);
      j = nextnegativeId(j, nums);
      ans.push_back(nums[i++]);
      ans.push_back(nums[j++]);
    }

    return ans;
  }
};