#include<bits/stdc++.h>
using namespace std;

class Solution {
public:

    vector<int> sieve(int n){
        vector<int> prime(n+1,1);
        prime[0] = prime[1] = 0;
        for (int i = 2; i*i <= n; i++) {
            if(prime[i]){
                for (int j = i*i; j <= n; j+=i) {
                    prime[j] = 0;
                }
            }
        }
        return prime;
    }

    vector<vector<int>> findPrimePairs(int n) {
        vector<int> prime = sieve(n);
        vector<vector<int>> ans;
        for (int i = 2; i <= n/2; i++) {
            if(prime[i] && prime[n-i]){
                ans.push_back({i,n-i});
            }
        }
        return ans;

    }
};

int main(){
    Solution s;
     int n = 10;
    vector<vector<int>> ans = s.findPrimePairs(n);
    for (auto &v : ans) {
        cout << v[0] << " " << v[1] << endl;
    }
    return 0;
}