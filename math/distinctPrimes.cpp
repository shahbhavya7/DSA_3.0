#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> primeFactors(int n)
    {
        vector<int> factors;
        for (int i = 2; i * i <= n; i++)
        {
            if (n % i == 0)
            {
                factors.push_back(i);
                while (n % i == 0) // to ensure we only add distinct prime factors,
                // we divide n by i until it's no longer divisible, so that we don't add the same prime factor multiple times
                //  for example, if n is 12, we will add 2 to the factors vector, and then divide n by 2 until n is no longer divisible by 2,
                //  which will give us n = 3, and we will add 3 to the factors vector as well
                {
                    n /= i;
                }
            }
        }
        if (n > 1)
            factors.push_back(n);
        return factors;
    }

    int distinctPrimeFactorsBrute(vector<int> &nums)
    {
        unordered_set<int> distinctPrimes; // using unordered_set to store distinct prime factors
        for (int num : nums)
        {
            vector<int> factors = primeFactors(num);
            for (int factor : factors)
            {
                distinctPrimes.insert(factor); // insert prime factor into the set
            }
        }
        return distinctPrimes.size(); // return the number of distinct prime factors
    }

    int distinctPrimeFactors(vector<int> &nums)
    {
        int cnt = 0;
        vector<int> primeCount(1001, 1); // to count the occurrences of each prime factor, we can use a vector of size 1001 (since the maximum value in nums is 1000)
        for (int i = 2; i <= 1000; i++)
        {
            if (primeCount[i] == 1)
            { // if i is a prime number
                for (int j = i * i; j <= 1000; j += i)
                {                      // Fix 1: start at i * 2, otherwise you mark the prime itself as 0
                    primeCount[j] = 0; // mark multiples of i as not prime
                }
            }
        }
        vector<int> primes; // to store all prime numbers up to 1000
        for (int i = 2; i <= 1000; i++)
        {
            if (primeCount[i] == 1)
            {                        // if i is a prime number
                primes.push_back(i); // add i to the list of prime numbers
            }
        }

        // Fix 2: Swap the loops. We want to count how many distinct primes divide AT LEAST one number in `nums`.
        for (int prime : primes)
        {
            for (int num : nums)
            {
                if (num % prime == 0)
                {          // if the current number is divisible by the prime number
                    cnt++; // increment the count of distinct prime factors
                    break; // move on to check the next prime as we only want to count distinct prime factors, 
                    //so we can break out of the loop once we find a prime factor that divides the current number
                }
            }
        }
        return cnt; // return the count of distinct prime factors
    }
};

int main()
{
    vector<int> nums = {2, 14, 19, 19, 5, 13, 18, 10, 15, 20};
    Solution sol;
    int result = sol.distinctPrimeFactors(nums);
    cout << "Number of distinct prime factors: " << result << endl;
    return 0;
}