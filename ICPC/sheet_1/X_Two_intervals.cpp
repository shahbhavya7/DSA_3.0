#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    int l1, r1, l2, r2;
    cin >> l1 >> r1 >> l2 >> r2;
    
    // Find the intersection boundaries
    int start = max(l1, l2);
    int end = min(r1, r2);

    // Check if the intersection is valid
    if (start <= end) {
        cout << start << " " << end << "\n";
    } else {
        cout << -1 << endl;
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