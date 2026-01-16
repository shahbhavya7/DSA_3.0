#include <bits/stdc++.h>
using namespace std;

class SolutionBrute
{
public:
    int majorityElementTwo(vector<int> &nums)
    {
        int n = nums.size();
        for (int i = 0; i < n; i++)
        {
            int cnt = 0;
            for (int j = 0; j < n; j++)
            {
                if (nums[i] == nums[j])
                {
                    cnt++;
                }
            }
            if (cnt > n / 2)
            {
                return {nums[i]};
            }
        }
        return -1;
    }
};

class SolutionBetter
{
public:
    int majorityElementTwo(vector<int> &nums)
    {
        unordered_map<int, int> mp;
        int n = nums.size();
        for (int i = 0; i < n; i++)
        {
            mp[nums[i]]++; // here first nums[i] is key and second is value, we are incrementing value by 1 each time we encounter nums[i]
        }
        for (auto it : mp)
        { // auto it is used to iterate through map
            if (it.second > n / 2)
            { // if any element's frequency i.e second is greater than n/2 then return that element i.e first
                return it.first;
            }
        }
        return -1;
    }
};

class SolutionOptimal
{
    public:
    int majorityElementTwo(vector<int> &nums){
        int cnt = 0;
        int el;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            if(cnt == 0){
                cnt = 1;
                el = nums[i];
            }
            else if(el == nums[i]){
                cnt++;
            }
            else{
                cnt--;
            }
        }

        int cnt1 = 0;
        for (int i = 0; i < n; i++) {
            if(nums[i] == el){
                cnt1++;
            }
        }
        if(cnt1 > n/2){
            return el;
        }
        return -1;
    }
};

int main()
{
    SolutionBrute obj;
    vector<int> nums = {2, 2, 1, 1, 1, 2, 2};
    cout << obj.majorityElementTwo(nums);
    cout << endl;

    SolutionBetter obj2;
    cout << obj2.majorityElementTwo(nums);
    cout << endl;

    SolutionOptimal obj3;
    cout << obj3.majorityElementTwo(nums);

    return 0;
}