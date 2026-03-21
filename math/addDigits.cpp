#include<bits/stdc++.h>
using namespace std;

class Solution { // this is concept of digital root where we can find the single digit sum of a number by using modulo 9
public:
    int addDigits(int num) {
        if (num == 0) return 0;
        if (num % 9 == 0) return 9;
        return num % 9;
    }
};

int main(){
    Solution sol;
    int num = 38;
    cout << sol.addDigits(num) << endl;
    return 0;
}