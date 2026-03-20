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
};

int main()
{
    int n = 29;
    Solution sol;
    if (sol.isPrime(n))
        cout << n << " is a prime number." << endl;
    else
        cout << n << " is not a prime number." << endl;
    return 0;
}