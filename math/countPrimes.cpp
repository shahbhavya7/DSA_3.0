#include<bits/stdc++.h>
using namespace std;

class SolutionBrute { 
// this will be a brute force solution with time complexity of O(n*sqrt(n)) as we are checking for each number less than n if it is prime or not
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

    int countPrimes(int n) {
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                count++;
            }
        }
        return count;      
    }
};

class Solution{ // this will be an optimized solution using the Sieve of Eratosthenes algorithm with time complexity of O(n log log n)
public:

    int countPrimes(int n){
        if (n <= 2) return 0; // there are no prime numbers less than 2
        int count = 0;
        vector<int> primes(n, 1); // initialize a vector of size n with all values set to 1 (true)
        primes[0] = primes[1] = 0; // 0 and 1 are not prime numbers, so we set their values to 0 (false)

        for (int i = 2; i * i < n; i++) { // we only need to loop up to sqrt(n) because any non-prime number will have a factor less than or equal to sqrt(n)
            if (primes[i]==1) { // if i is prime
                for (int j = i * i; j < n; j += i) { // we start marking multiples of i from i*i because any smaller multiple of i would have already been marked by a smaller prime factor
                    primes[j] = 0; // mark multiples of i as non-prime
                }
            }
        }
        for (int i = 2; i < n; i++) {
            if (primes[i] == 1) { // if i is prime
                count++;
            }
        }
        return count;
    }

};

int main(){
    int n = 10;
    Solution sol;
    int result = sol.countPrimes(n);
    cout << "Number of prime numbers less than " << n << ": " << result << endl;
    return 0;
}