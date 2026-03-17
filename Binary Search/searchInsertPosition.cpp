#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int searchInsert(vector<int> &nums, int target)
    {
        int low = 0;
        int high = nums.size() - 1;
        while (low <= high)
        {
            int mid = low + (high - low) / 2; // To avoid potential overflow we use this formula instead of (low+high)/2
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] < target)
                low = mid + 1;
            else
                high = mid - 1;
        }
        return low; // low is the position where target would be inserted
    }
};

int main()
{
    vector<int> nums = {1, 3, 5, 6};
    int target = 2;
    Solution sol;
    cout << sol.searchInsert(nums, target) << "\n"; // Output: 2
    return 0;
}