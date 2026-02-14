#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    long double r;
    cin >> r;
    long double area = 3.141592653 * r * r;
    cout << fixed << setprecision(9) << area << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // int t;
    // cin >> t;
    // while (t--) {
    //     solve();
    // }
    solve();
    return 0;
}