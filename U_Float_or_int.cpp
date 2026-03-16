#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    double n;
    cin >> n;
    if (n == (int)n)
        cout << "int " << (int)n << endl;
    else
        cout << "float " << (int)n <<" "<< n - (int)n<< endl;
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