#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        int n = x, rev = 0;
        while (n > 0) {
            rev = rev * 10 + n % 10; // Reverse the number
            n /= 10; // Remove the last digit
        }
        return rev == x; // Check if the reversed number is equal to the original
    }
};

int main(){
    Solution sol;
    int x = 121; // Example input
    cout << sol.isPalindrome(x) << endl; // Output: 1 (true, since 121 is a palindrome)
    return 0;
}