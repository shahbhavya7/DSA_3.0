#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    int n;
    cin >> n;
    
    int current_max = -1; // Since elements are >= 1, this is a safe start
    int operations = 0;
    
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val;
        
        // If the current element is greater than or equal to the max we've seen so far
        if (val >= current_max) {
            current_max = val;
            operations++;
        }
    }
    
    cout << operations << "\n";
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