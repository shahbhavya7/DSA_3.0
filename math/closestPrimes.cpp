#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> sieve(int n)
    {
        vector<int> prime(n + 1, 1);
        prime[0] = prime[1] = 0;
        for (int i = 2; i * i <= n; i++)
        {
            if (prime[i] == 1)
            {
                for (int j = i * i; j <= n; j += i)
                {
                    prime[j] = 0;
                }
            }
        }
        return prime;
    }

    vector<int> closestPrimes(int left, int right)
    {
        vector<int> sieves = sieve(right);
        vector<int> primes;
        for (int i = left; i <= right; i++)
        {
            if (sieves[i] == 1)
            {
                primes.push_back(i);
            }
        }
        if (primes.size() < 2)
        {
            return {-1, -1};
        }
        int n = primes.size();
        int minDiff = INT_MAX;
        vector<int> result = {-1, -1};
        for (int i = 1; i < n; i++)
        {
            int diff = primes[i] - primes[i - 1];
            if (diff < minDiff)
            {
                minDiff = diff;
                result = {primes[i - 1], primes[i]};
            }
        }
        return result;
    }
};

int main()
{
    Solution sol;
    int left = 10, right = 19;
    vector<int> result = sol.closestPrimes(left, right);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}