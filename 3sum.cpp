#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<vector<int>> threeSumBrute(vector<int> &nums)
    {
        int n = nums.size();
        set<vector<int>> resultSet; // Using set to avoid duplicate triplets
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                for (int k = j + 1; k < n; k++)
                {
                    if (nums[i] + nums[j] + nums[k] == 0)
                    {
                        vector<int> trip = {nums[i], nums[j], nums[k]};
                        sort(trip.begin(), trip.end());
                        resultSet.insert(trip);
                    }
                }
            }
        }
        vector<vector<int>> result(resultSet.begin(), resultSet.end()); // Convert set to vector
        return result;
    }
    vector<vector<int>> threeSumBetter(vector<int> &nums)
    {
        int n = nums.size();
        set<vector<int>> resSet; // Using set to avoid duplicate triplets
        for (int i = 0; i < n; i++)
        {
            set<int> seen;
            for (int j = i + 1; j < n; j++)
            {
                int third = -(nums[i] + nums[j]);
                if (seen.find(third) != seen.end())
                {
                    vector<int> trip = {nums[i], nums[j], third};
                    sort(trip.begin(), trip.end());
                    resSet.insert(trip);
                }
                seen.insert(nums[j]);
            }
        }
        vector<vector<int>> result(resSet.begin(), resSet.end());
        return result;
    }
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        int n = nums.size();

        for (int i = 0; i < n; i++)
        {
            if (i > 0 && nums[i] == nums[i - 1])
                continue; // Skip duplicate elements for the first number
            int left = i + 1;
            int right = n - 1;

            while (left < right)
            {
                int sum = nums[i] + nums[left] + nums[right];
                if(sum == 0){
                    res.push_back({nums[i], nums[left], nums[right]});
                    left++;
                    right--;

                    while(left < right && nums[left] == nums[left - 1]) left++; // Skip duplicates for the second number
                    while(left < right && nums[right] == nums[right + 1]) right--; // Skip duplicates for the third number
                }
                else if (sum < 0) left++; // as sorted array so move left to increase sum
                else right--; // move right to decrease sum
            }
        }
        return res;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {-1, 0, 1, 2, -1, -4};
    vector<vector<int>> result = sol.threeSum(nums);
    for (const auto &triplet : result)
    {
        for (int num : triplet)
        {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}