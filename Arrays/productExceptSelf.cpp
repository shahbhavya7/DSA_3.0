#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> productExceptSelfBrute(vector<int> &nums)
    {
        vector<int> ans;
        int n = nums.size();
        for (int i = 0; i < n; i++)
        {
            int product = 1;
            for (int j = 0; j < n; j++)
            {
                if (i != j)
                {
                    product *= nums[j];
                }
            }
            ans.push_back(product);
        }
        return ans;
    }

    vector<int> productExceptSelf(vector<int> &nums)
    {
        vector<int> ans(nums.size(), 1);
        int left = 1;
        for (int i = 0; i < nums.size(); i++)
        {
            ans[i] *= left;
            left *= nums[i];
        }
        int right = 1;
        for (int i = nums.size() - 1; i >= 0; i--)
        {
            ans[i] *= right;
            right *= nums[i];
        }
        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {1, 2, 3, 4};
    vector<int> result = sol.productExceptSelf(nums);
    for (int i : result)
    {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}