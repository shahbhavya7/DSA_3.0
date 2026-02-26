#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    // Check distance from 0 to first station
    int ans = a[0]; 
    
    // Check distances between stations
    for (int i = 0; i < n - 1; i++) {
        ans = max(ans, a[i + 1] - a[i]);
    }
    
    // Check the last segment (to m and back) which is 2 * (m - last station)
    ans = max(ans, 2 * (m - a[n - 1]));
    
    cout << ans << "\n";
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