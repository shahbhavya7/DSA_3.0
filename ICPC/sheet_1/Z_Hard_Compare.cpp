#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve()
{
    long double a, b, c, d;
    cin >> a >> b >> c >> d;
    long double res1 = b * log(a);
    long double res2 = d * log(c);
    if (res1 > res2)
        cout << "YES\n";
    else
        cout << "NO\n";
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // int t;
    // cin >> t;
    // while (t--) {
    solve();
    // }
    return 0;
}