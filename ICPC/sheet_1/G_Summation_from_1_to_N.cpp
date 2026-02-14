#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    long long n;
    cin >> n;
    long long sum = n * (n + 1) / 2; // Using the formula for the sum of the first n natural numbers
    cout << sum << "\n"; // Output the result
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