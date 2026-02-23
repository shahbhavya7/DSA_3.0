#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    bool containsNearbyDuplicate(vector<int> &nums, int k)
    {
        unordered_map<int, int> hash;
        for (int i = 0; i < nums.size(); i++)
        {
            if (hash.count(nums[i]) && i - hash[nums[i]] <= k) 
            // hash.count(nums[i]) checks if nums[i] is already in the hash map, and i - hash[nums[i]] <= k 
            // checks if the distance between the current index and the last index of nums[i] is less than or 
            // equal to k
            {
                return true;
            }
            hash[nums[i]] = i;
        }
        return false;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {1, 2, 3, 1};
    int k = 3;
    cout << sol.containsNearbyDuplicate(nums, k) << endl;
    return 0;
}