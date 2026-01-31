#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> smallerNumbersThanCurrent(vector<int> &nums)
    {
        map<int, int> mp;   // map to store the first occurrence index of each number from behind
        vector<int> result = nums; // result vector initialized with nums
        sort(result.begin(), result.end()); // sort the result vector
        int n = nums.size();

        for (int i = n - 1; i >= 0; i--)
        {
            mp[result[i]] = i; // store the first occurrence index of each number from behind
            // this ensures that for duplicate numbers, we store the index of their last occurrence in the sorted array
        }
        for (int i = 0; i < n; i++)
        {
            result[i] = mp[nums[i]]; // replace each number in nums with its count of smaller numbers
        }
        return result; // return the result vector
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {8, 1, 2, 2, 3};
    vector<int> result = sol.smallerNumbersThanCurrent(nums);
    cout << "Number of smaller elements than current: ";
    for (int count : result)
    {
        cout << count << " ";
    }

    return 0;
}