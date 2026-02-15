#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    int a,b,c;
    cin >> a >> b >> c;
    int mx = max(a,max(b,c));
    int mn = min(a,min(b,c));
    cout << mn<<" "<<mx<<endl;
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