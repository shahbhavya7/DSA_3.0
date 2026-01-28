#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int myAtoi(string s) {
        int n = s.size();
        int i = 0;
        while(i < n && s[i] == ' ') i++;
        bool neg = false;
        if(i < n && (s[i] == '+' || s[i] == '-')){ // check for sign
            if(s[i] == '-') neg = true;
            i++;
        }
        long long ans = 0;
        while(i < n && isdigit(s[i])){ // isdigit checks if a character is a digit
            ans = ans * 10 + (s[i] - '0'); // subtracting '0' converts char to int
            if(!neg && ans > INT_MAX) return INT_MAX; // if not negative and exceeds INT_MAX return INT_MAX
            if(neg && -ans < INT_MIN) return INT_MIN; // if negative and exceeds INT_MIN return INT_MIN
            i++;
        }
        if(neg) ans = -ans;
        return (int)ans; 
    }
};

int main(){
    Solution sol;
    string str = "   -42";
    cout << sol.myAtoi(str) << endl; // Output: -42
    return 0;
}