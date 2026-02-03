#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int m = s.size();
        int n = t.size();
        int j = 0;
        if (m == 0) return true;
        for (int i = 0; i < n; i++) {
            if (s[j] == t[i]) {
                j++;
            }
            if (j == m) {
                return true;
            }
        }
        return false;
    }
};

int main(){
    Solution sol;
    string s = "abc";
    string t = "ahbgdc";
    bool result = sol.isSubsequence(s, t);
    cout << (result ? "true" : "false") << endl;

    return 0;
}