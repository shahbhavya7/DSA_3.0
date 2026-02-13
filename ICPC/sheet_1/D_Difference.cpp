#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    long long a,b,c,d;
    cin >> a >> b >> c >> d;
    cout << "Difference = " << (a*b) - (c*d) << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}