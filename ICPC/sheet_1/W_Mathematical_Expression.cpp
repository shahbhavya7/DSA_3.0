 #include <bits/stdc++.h>
 using namespace std;
 
 #define ll long long
 #define pb push_back
 
 void solve() {
    int a, b,c;
    char s,q;
    cin >> a >> s >> b >> q >> c;
    if (s == '+' ){
        if (a + b == c) {
            cout << "Yes\n";
        } else {
            cout << a + b << "\n";
        }
    } else if (s == '-') {
        if (a - b == c) {
            cout << "Yes\n";
        } else {
            cout << a - b << "\n";
        }
    }
        else if (s == '*') {
            if (a * b == c) {
                cout << "Yes\n";
            } else {
                cout << a * b << "\n";
            }
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