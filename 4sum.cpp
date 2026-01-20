#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<vector<int>> fourSum(vector<int> &nums, int target)
    {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        int n = nums.size();

        for (int i = 0; i < n; i++)
        {
            if (i > 0 && nums[i] == nums[i - 1]) // if i has done first iteration and current iteration is same as previous
                continue; // Skip duplicate elements for the first number
            for (int j = i + 1; j < n; j++)
            {
                if (j > i + 1 && nums[j] == nums[j - 1]) // if j has done first iteration after i and current iteration is same as previous
                    continue; // Skip duplicate elements for the second number
                int left = j + 1;
                int right = n - 1;

                while (left < right)
                {
                    long long sum = (long long)nums[i] + nums[j] + nums[left] + nums[right]; // To prevent integer overflow convert int to long long
                    if (sum == target)
                    {
                        res.push_back({nums[i], nums[left], nums[right], nums[j]});
                        left++;
                        right--;

                        while (left < right && nums[left] == nums[left - 1])
                            left++; // Skip duplicates for the second number
                        while (left < right && nums[right] == nums[right + 1])
                            right--; // Skip duplicates for the third number
                    }
                    else if (sum < target)
                        left++; // as sorted array so move left to increase sum
                    else
                        right--; // move right to decrease sum
                }
            }
        }
        return res;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {1, 0, -1, 0, -2, 2};
    int target = 0;
    vector<vector<int>> result = sol.fourSum(nums, target);
    for (const auto &quadruplet : result)
    {
        for (int num : quadruplet)
        {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}