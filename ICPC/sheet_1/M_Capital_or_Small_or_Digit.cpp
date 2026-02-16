#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    char c;
    cin >> c;
    if (c >= 'A' && c <= 'Z') {
        cout << "ALPHA" << endl;
        cout << "IS CAPITAL" << endl;
    } else if (c >= 'a' && c <= 'z') {
        cout << "ALPHA" << endl;
        cout << "IS SMALL" << endl;
    } else if (c >= '0' && c <= '9') {
        cout << "IS DIGIT" << endl;
    } else {
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