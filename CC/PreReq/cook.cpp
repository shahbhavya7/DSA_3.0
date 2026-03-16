#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    int n;
    cin >> n;
    vector<int> finish(n);
    vector<int> cook(n+1);
    cook[0] = 0; // Assuming the first cook time is 0 for the first dish
    for(int i=1; i<n; i++) {
        cin >> finish[i];
    }
    for(int i=0; i<n; i++) {
        cin >> cook[i];
    }
    int ans = 0;
    for(int i=0; i<n; i++) {
        if((finish[i-1] - finish[i]) > cook[i]) { 
            ans++;
        }
    }
    cout << ans << endl;
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