#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    int n;
    cin >> n;
    map<int, int> mp; // Keys are sorted automatically
    for(int i=0; i<n; i++) {
        int x;
        cin >> x;
        mp[x]++;
    }
    
    // Print unique elements (sorted)
    bool first = true;
    for(auto it : mp) {
        if(!first) cout << " ";
        cout << it.first;
        first = false;
    }
    cout << endl;

    // Print frequencies corresponding to sorted unique elements
    first = true;
    for(auto it : mp) {
        if(!first) cout << " ";
        cout << it.second;
        first = false;
    }
    cout << endl;
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