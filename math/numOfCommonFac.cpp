#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int commonFactorsBrute(int a, int b) {
        int minval = min(a, b); 
        int count = 0;
        for (int i = 1; i <= minval; i++) {
            if (a % i == 0 && b % i == 0) { // start from 1 as 1 is a common factor of all numbers
                count++; // Increment count if i is a common factor of both a and b
            }
        }
        return count; // Return the total count of common factors
    }

    int commonFactors(int a, int b){
        // the concept is to find the greatest common divisor (GCD) of a and b, and then count the number of factors of that GCD, 
        // common factors of gcd will be common factors of a and b and beyond gcd there will be no common factors of a and b
        // so we iterate only till gcdval and count the factors of gcdval, sq root is to optimize the counting of factors, as factors come in pairs, 
        // we can count both factors at once when we find a factor less than or equal to the square root of gcdval
        int count  = 0;
        int gcdval = __gcd(a, b); // Calculate the greatest common divisor (GCD) of a and b
        for (int i = 1; i *i <= gcdval; i++) {
            if (gcdval % i == 0) { // Check if i is a factor of the GCD
                count++; 
                if (i != gcdval / i) { 
                    count++; 
                }
            }
        }
        return count; 
    }
};

int main(){
    Solution sol;
    int a = 12, b = 6;
    int result = sol.commonFactors(a, b);
    cout << result << endl; // print the number of common factors between a and b
    return 0;
}