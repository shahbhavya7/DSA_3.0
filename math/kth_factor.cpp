#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int kthFactorI(int n, int k)
    {   
        vector<int> divisors;
        for (int i = 1; i <= sqrt(n); i++)
        {
            if (n % i == 0)
            {
                divisors.push_back(i);
                if (i != n / i)
                {
                    divisors.push_back(n / i); // add complementary divisor if it's different from i i.e for 36 when i=6, we don't want to add 6 again as
                    // it's the same divisor, but for i=2 we also add 18 which is n/i
                }
            }
        }
        sort(divisors.begin(), divisors.end());
        if (k > divisors.size())
        {
            return -1; // If k is greater than the number of divisors, return -1
        }
        return divisors[k - 1]; // Return the k-th factor (1-indexed)
    }

    int kthFactor(int n, int k)
    {
        int count = 0;
        for (int i = 1; i <= n; i++)
        {
            if (n % i == 0)
            {
                count++;
                if (count == k)
                {
                    return i; 
                }
            }
        }
        return -1; 
    }
};

int main()
{
    int n = 12, k = 3;
    Solution sol;
    cout << sol.kthFactor(n, k) << "\n"; // Output: 3 (the factors of 12 are 1, 2, 3, 4, 6, 12)
    return 0;
}