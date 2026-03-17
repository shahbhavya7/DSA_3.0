#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool checkPerfectNumberBrute(int num) {
        int sum = 0;
        for (int i = 1; i <= num/2; i++) {
            if (num % i == 0){
                sum = sum + i;
            }
        }
        return sum == num;
    }

    bool checkPerfectNumber(int num) {
        if (num <= 1) return false; // Perfect numbers are greater than 1
        int sum = 1; // Start with 1, which is a proper divisor
        for (int i = 2; i <= sqrt(num); i++) { // Check divisors up to the square root of num
            if (num % i == 0) {
                sum += i; // Add the divisor
                if (i != num / i) { // Add the complementary divisor if it's different eg. for 28, when i=2, we also add 14
                    sum += num / i;
                }
            }
        }
        return sum == num;
    }
};

int main(){
    int num = 28;
    Solution sol;
    cout << sol.checkPerfectNumber(num) << "\n"; // Output: 1 (true)
    return 0;
}