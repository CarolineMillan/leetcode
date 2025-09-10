#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash;
        for (int i=0; i < nums.size(); i++) {
            // first check if we've found the answer
            if (hash.find(target - nums[i]) != hash.end()) {
                vector<int> ans = {i, hash.at(target - nums[i])};
                return ans;
            }
            hash[nums[i]] = i;
        }
        return {};
    }
};