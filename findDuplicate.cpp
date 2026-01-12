#include <bits/stdc++.h>
using namespace std;

class SolutionBrute
{
public:
    int findDuplicate(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 1; i++)
        {
            if (nums[i] == nums[i + 1])
            {
                return nums[i];
            }
        }
        return -1; // Return a default value if no duplicate is found
    }
};

class SolutionBetter
{
public:
    int findDuplicate(vector<int> &nums)
    {
        int n = nums.size();
        vector<int> freq(n + 1, 0);
        for (int i = 0; i < n; i++)
        {
            if (freq[nums[i]] == 0)
            {
                freq[nums[i]]++;
            }
            else
            {
                return nums[i];
            }
        }
        return -1; // Return a default value if no duplicate is found
    }
};

class SolutionOptimal
{
    public:
        int findDuplicate(vector<int> &nums)
    {
        int n = nums.size();
        int slow = nums[0];
        int fast = nums[0];

        
    }
};

int main()
{
    SolutionBrute sol;
    vector<int> nums = {3, 1, 3, 4, 2};
    int duplicate = sol.findDuplicate(nums);
    cout << "Duplicate number is: " << duplicate << endl;

    SolutionBetter solBetter;
    nums = {3, 1, 3, 4, 2};
    duplicate = solBetter.findDuplicate(nums);
    cout << "Duplicate number is: " << duplicate << endl;

    return 0;
}