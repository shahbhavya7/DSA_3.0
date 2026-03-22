#include<bits/stdc++.h>
using namespace std;

class Solution {
public:

    vector<int> sieve(int n){
        vector<int> prime(n+1, 1); // initialize a vector of size n+1 with all values set to 1 (true)
        prime[0] = prime[1] = 0; // 0 and 1 are not prime numbers, so we set their values to 0 (false)
        for (int i = 2; i * i <= n; i++) {
            if (prime[i] == 1){
                for (int j = i *i; j <= n; j += i) {
                    prime[j] = 0; // mark multiples of i as non-prime
                }
            }
        }
        return prime;
    }

    int maximumPrimeDifference(vector<int>& nums) {
        int n  = nums.size();
        vector<int> prime = sieve(101); // get the prime numbers up to 1000   
        int maxDiff = 0;
        int firstPrime = -1;
        for (int i = 0; i < n; i++) {
            if (prime[nums[i]] == 1){
                if (firstPrime == -1){
                    firstPrime = i; // Only set this once when the first prime is found
                } else {
                    maxDiff = i - firstPrime; // Calculate distance from the very first prime
                }
            }
        }
        return maxDiff;
    }
};

int main(){
    Solution sol;
    vector<int> nums = {4,2,9,5,3};
    int result = sol.maximumPrimeDifference(nums);
    cout << result << endl; // print the maximum difference between the indices of two prime numbers
    return 0;
}