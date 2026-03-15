#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int minSubArrayLenBrute(int target, vector<int> &nums)
    { // Brute Force o(n^2)
        int n = nums.size();
        int sum = 0;
        int minLength = INT_MAX;
        for (int i = 0; i < n; i++)
        {
            sum = 0;
            for (int j = i; j < n; j++)
            {
                sum += nums[j];
                if (sum >= target)
                {
                    minLength = min(minLength, j - i + 1); // +1 because we are counting the length of the subarray
                    break;
                }
            }
        }
        if (minLength == INT_MAX)
            return 0;
        return minLength;
    }

    int minSubArrayLen(int target, vector<int> &nums)
    {
        int n = nums.size();
        int sum = 0;
        int minLength = INT_MAX;
        int left = 0;
        int right = 0;
        while (right < n)
        {
            sum = sum + nums[right];
            while (sum >= target)
            {
                minLength = min(minLength, right - left + 1);
                sum = sum - nums[left];
                left++;
            }
            right++;
        }
        if (minLength == INT_MAX)
            return 0;
        return minLength;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {2, 3, 1, 2, 4, 3};
    int target = 7;
    cout << sol.minSubArrayLen(target, nums) << endl; // Output: 2
    return 0;
}