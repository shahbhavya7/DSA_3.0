#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> PrimeFactors(int n)
    {
        vector<int> factors;
        for (int i = 2; i * i <= n; i++)
        {
            while (n % i == 0)
            {
                factors.push_back(i);
                n /= i;
            }
        }
        if (n > 1)
            factors.push_back(n);
        return factors;
    }

    int mySqrt(int x)
    {
        vector<int> factors = PrimeFactors(x);
        int result = 1;
    }
};

int main()
{

    return 0;
}