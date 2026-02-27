#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    int maxd = 0;
    
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        if (a[i] > maxd) {
            maxd = a[i];
        }
    }
    int winners = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] == maxd) {
            winners++;
        }
    }
    
    cout << winners << "\n";
}

int main() {
    // Optimize standard I/O operations for performance
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}