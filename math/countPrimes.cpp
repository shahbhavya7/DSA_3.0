#include<bits/stdc++.h>
using namespace std;

class SolutionBrute {
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


int main(){
    int n = 10;
    SolutionBrute sol;
    int result = sol.countPrimes(n);
    cout << "Number of prime numbers less than " << n << ": " << result << endl;
    return 0;
}