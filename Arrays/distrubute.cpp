#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int distMoney(int m, int c) {
        int val = m - c;
        int count = 0;
        if(val<0) return -1;
        else{
            if(val < 7) return 0;
            else{
                count  = val/7;
                int rem = val%7;
                if(rem==3 && count==c-1) count--;
                if(count==c && rem>0) count--;
                if(count>c) return c-1;
                return count;
            }
        }
    }
};

int main(){
    Solution sol;
    int money = 20;
    int children = 3;
    int result = sol.distMoney(money, children);
    cout << "Maximum children with 8 dollars: " << result << endl;
    return 0;
}