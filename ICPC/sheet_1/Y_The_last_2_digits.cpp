#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    ll a, b, c, d;
    cin >> a >> b >> c >> d;
    
    // Apply modulo at each step to prevent overflow
    ll ans = (a % 100 * b % 100 * c % 100 * d % 100) % 100;
    
    // Print with leading zero if the number is less than 10
    if (ans < 10) cout << "0" << ans << endl;
    else cout << ans << endl;
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