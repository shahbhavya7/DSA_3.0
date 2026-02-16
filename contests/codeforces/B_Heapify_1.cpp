#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

int get_odd(int n) 
{
    while (n % 2 == 0)
    {
        n /= 2;
    }
    return n;
}

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

    for (int i = 0; i < n; i++)
    {
        // In 1-based indexing, the position is i + 1
        // The value at this position is nums[i]
        // They must belong to the same swap component (same odd part)
        if (get_odd(nums[i]) != get_odd(i + 1))
        {
            cout << "NO" << endl;
            return;
        }
    }
    cout << "YES" << endl;
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