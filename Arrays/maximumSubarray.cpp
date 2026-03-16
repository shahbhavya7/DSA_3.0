#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int maxi = INT_MIN;
        int n = nums.size();

        for (int i = 0; i < n; i++)
        {
            for (int j = i; j < n; j++)
            {
                int sum = 0;
                for (int k = i; k <= j; k++)
                {
                    sum = sum + nums[k];
                }
                maxi = max(maxi, sum);
            }
        }
        return maxi;
    }
    int maxSubArrayBetter(vector<int> &nums)
    {
        int maxi = INT_MIN;
        int n = nums.size();
        for (int i = 0; i < n; i++)
        {
            int sum = 0;
            for (int j = i; j < n; j++)
            {
                sum = sum + nums[j];
                maxi = max(maxi, sum);
            }
        }
        return maxi;
    }
    int maxsubArrayOptimal(vector<int> &nums) // if
    {
        int n = nums.size();
        int maxi = INT_MIN;
        int sum = 0;
        for (int i = 0; i < n; i++)
        {
            sum += nums[i];
            maxi = max(maxi, sum);
            if (sum < 0)
            {
                sum = 0;
            }
        }
        return maxi;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int result = sol.maxSubArray(nums);
    cout << "Maximum Subarray Sum: " << result << endl;
    int resultBetter = sol.maxSubArrayBetter(nums);
    cout << "Maximum Subarray Sum (Better): " << resultBetter << endl;
    int resultOptimal = sol.maxsubArrayOptimal(nums);
    cout << "Maximum Subarray Sum (Optimal): " << resultOptimal << endl;
    return 0;
}