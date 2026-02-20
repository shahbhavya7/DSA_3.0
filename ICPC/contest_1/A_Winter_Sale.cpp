#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    float x,p;
    cin >> x >> p;
    float price = p/(1-(x/100));
    cout << fixed << setprecision(2) << price << endl;
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