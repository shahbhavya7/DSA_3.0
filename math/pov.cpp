#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    double power(double x, long long n)
    {
        if (n == 0)
            return 1.0;
        if (n == 1)
            return x;
        if (n % 2 == 0)
        {  // if n is even
            return myPow(x * x, n / 2); // multiply x twice and reduce n to half
        }
        else
        {
            return x * myPow(x, n - 1); // reduce n by 1 and multiply x once
        }
    }
    double myPow(double x, int n)
    {
        long long num = n; // converting to long long to avoid overflow for -2^31
        if (num < 0)
        {
            return (1.0 / power(x,-1 * num));
        }
        return power(x, num);
    }
};

int main()
{

    Solution sol;
    double x = 2.00000;
    int n = 10;
    double result = sol.myPow(x, n);
    cout << "Result: " << result << endl;

    return 0;
}