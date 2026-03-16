#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    int n,k;
    cin >> n >> k;
    vector<int> arr(n);
    vector<int> ans(n);
    for(int i=0; i<n; i++) {
        cin >> arr[i];
    }
    ans = arr; // Initialize ans with original revenues
    for (int i = 0; i < n; i++) {
        if(ans[i] > k) ans[i] = k;
    }
    long long loss = 0;
    for(int i=0; i<n; i++) {
        loss += (arr[i] - ans[i]);
    }
    cout << loss << endl;
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