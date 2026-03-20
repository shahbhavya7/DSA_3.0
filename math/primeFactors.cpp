#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    bool isPrime(int n)
    {
        if (n <= 1)
            return false; // 0 and 1 are not prime numbers
        for (int i = 2; i <= sqrt(n); i++)
        {
            if (n % i == 0)
                return false; // n is divisible by a number other than 1 and itself
        }
        return true; // n is prime
    }

    vector<int> primeFactors(int n)
    {
        vector<int> factors;
        for (int i = 2; i <= sqrt(n); i++)
        {
            if (n % i == 0)
            {
                if (isPrime(i))
                {
                    factors.push_back(i);
                }
                if (i != n / i && isPrime(n / i))
                {
                    factors.push_back(n / i);
                }
            }
        }
        if (n != 1)
            factors.push_back(n); // if n is prime, we need to add it to the factors vector as well
        return factors;
    }
};

int main()
{
    int n = 156;
    Solution sol;
    vector<int> factors = sol.primeFactors(n);
    cout << "Prime factors of " << n << ": ";
    for (int factor : factors)
    {
        cout << factor << " ";
    }
    return 0;
}