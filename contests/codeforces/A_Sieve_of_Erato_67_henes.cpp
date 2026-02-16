#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve()
{
    int n;
    cin >> n;
    vector<int> nums;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        nums.push_back(x);
    }
    bool one = false;
    bool sixty_seven = false;
    for (int i : nums)
    {
        if (i == 1)
        {
            one = true;
        }
        if (i == 67)
        {
            sixty_seven = true;
        }
    }
    if (sixty_seven)
    {
        cout << "YES" << endl;
    }
    else
    {
        cout << "NO" << endl;
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