#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    int a, b, c;
    cin >> a >> b >> c;
    vector<int> v = {a, b, c};
    vector<int> sorted = v;
    sort(sorted.begin(), sorted.end());
    for (int i : sorted)
        cout << i << endl;
    cout << endl;
    for (int i : v)
        cout << i << endl; 
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