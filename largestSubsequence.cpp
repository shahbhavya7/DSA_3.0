#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int longestConsecutive(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());
        int longestStreak = 0;
        int currentStreak = 1;
        int n = nums.size();

        for (int i = 0; i < n-1; i++) {
            if (nums[i] != nums[i+1]){
                if (nums[i] + 1 == nums[i+1]) {
                    currentStreak += 1;
                }
                else {
                    longestStreak = max(longestStreak, currentStreak);
                    currentStreak = 1;
                }
            }
        }
        if (n == 0) return 0;
        return max(longestStreak, currentStreak);
    }

    int longestConsecutiveOptimal(vector<int>& nums) {}
};

int main()
{
    Solution sol;
    vector<int> nums = {100, 4, 200, 1, 3, 2};
    int result = sol.longestConsecutive(nums);
    cout << "Length of the longest consecutive elements sequence: " << result << endl;

    return 0;
}