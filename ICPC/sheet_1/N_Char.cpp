#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    char c;
    cin >> c;
    if (c >= 'A' && c <= 'Z') {
        cout<<static_cast<char>(c+32) << endl; 
        
    }
    else if (c >= 'a' && c <= 'z') {
        cout<<static_cast<char>(c-32) << endl;
    }
     else if (c >= '0' && c <= '9') {
        cout << c << endl;
}
    else {
        cout << "Special Character" << endl;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // int t;
    // cin >> t;
    // while (t--) {
        solve();
    // }
    return 0;
}