#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve()
{
    int n;
    string s;
    cin >> n >> s;
    int k = 0;
    bool hasSame = false;
    for (int i = 0; i < n; i++)
    {
        if (s[i] != s[(i + 1) % n])
        {
            k++;
        }
        else
        {
            hasSame = true;
        }
    }
    if (hasSame)
    {
        cout << k + 1 << endl;
    }
    else
    {
        cout << k << endl;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}