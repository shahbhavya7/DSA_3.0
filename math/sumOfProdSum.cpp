#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int subtractProductAndSum(int n) {
        int m = n;
        int sum = 0;
        while(m > 0){
            int digit = m % 10; 
            sum += digit; 
            m /= 10; 
        }
        int product = 1;
        m = n; 
        while(m > 0){
            int digit = m % 10; 
            product *= digit; 
            m /= 10; 
        }
        return product - sum; 
    }
};

int main(){
    int n = 234;
    Solution sol;
    cout << sol.subtractProductAndSum(n) << "\n"; // Output: 15
    return 0;
}