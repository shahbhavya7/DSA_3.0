#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        int n = nums.size();
        int k = n; // k is the length of array after removing duplicates
        if (n == 0)
            return 0;
        int el = nums[0];
        int count = 1; // count of current element
        for (int i = 1; i < n; i++)
        {
            if (el == nums[i])
            {
                count++;
                if (count > 2)
                {
                    // Shift elements to the left
                    for (int j = i; j < n - 1; j++)
                    {
                        nums[j] = nums[j + 1];
                    }
                    n--; // Reduce the size of the array
                    k--; // Reduce the count of unique elements
                    i--; // Stay at the same index to check the new element at this position
                }
            }
            else
            {
                el = nums[i];
                count = 1;
            }
        }
        return k;
    }

    int removeDuplicatesOptim(vector<int> &nums)
    {
        int i = 0;
        // int ele= nums[0];
        for (auto ele : nums)
        {
            if (i == 0 || i == 1 || nums[i - 2] != ele)
            {
                nums[i] = ele;
                i++;
            }
        }
        return i;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {0, 0, 1, 1, 1, 1, 2, 3, 3};
    int k = sol.removeDuplicates(nums);
    cout << "Length after removing duplicates: " << k << endl;
    return 0;
}