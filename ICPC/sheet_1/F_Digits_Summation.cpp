#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    long long m, n;
    cin >> m >> n;
    long long sum = 0;
    m = m%10; // Get the last digit of m
    n = n%10; // Get the last digit of n
    sum = m + n; // Sum of the last digits
    cout << sum<< "\n"; // Output the last digit of the sum
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