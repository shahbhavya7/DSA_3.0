#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    if (n % 2 != 0) {
        cout << "NO\n";
        return;
    }

    vector<char> st;
    
    for (char c : s) {
        if (!st.empty() && st.back() == c) {
            st.pop_back(); 
        } else {
            st.push_back(c); 
        }
    }
    if (st.empty()) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}