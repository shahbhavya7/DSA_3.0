#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back
#define all(v) v.begin(), v.end()

void solve()
{
    long long a, b;
    cin >> a >> b;
    cout << a << " + " << b << " = " << a + b << "\n";
    cout << a << " * " << b << " = " << a * b << "\n";
    cout << a << " - " << b << " = " << a - b << "\n";
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}