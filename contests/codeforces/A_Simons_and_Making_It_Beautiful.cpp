#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int maxVal = INT_MIN;
    int maxIdx = -1;
    for (int i = 0; i < n; i++) {
        if (a[i] > maxVal) {
            maxVal = a[i];
            maxIdx = i;
        }
    }
    swap(a[0], a[maxIdx]);
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << "\n";
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