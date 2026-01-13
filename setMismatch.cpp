#include <bits/stdc++.h>
using namespace std;

class SolutionOptimal
{
public:
    vector<int> findErrorNums(vector<int> &nums)
    {
        long long n = nums.size();
        long long SN = (n * (n + 1))/2; // Sum of first n natural numbers
        long long S2N = (n * (n + 1) * (2*n + 1))/6; // Sum of squares of first n natural numbers

        long long S = 0; // Actual sum of elements in the array
        long long S2 = 0; // Actual sum of squares of elements in the array

        for(long long nums:nums){
            S = S + nums;
            S2 = S2 + (long long)nums * (long long)nums;
        }
        long long diff = SN - S; // missing - duplicate
        long long sum = S2N - S2; // missing^2 - duplicate^2
        sum = sum / diff; // missing + duplicate by property of X^2 - Y^2 = (X - Y)(X + Y)
        long long missing = (diff + sum) / 2; //  by putting equations together
        long long duplicate = missing - diff;
        return {(int)duplicate, (int)missing};
    }
};

int main()
{
    SolutionOptimal sol;
    vector<int> nums = {2, 2}; // duplicate: 2, missing: 3
    vector<int> result = sol.findErrorNums(nums);
    cout << "Duplicate: " << result[0] << ", Missing: " << result[1] << endl;
    return 0;
}