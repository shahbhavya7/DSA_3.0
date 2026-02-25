#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    long long a,b,k;
    cin>>a>>b>>k;
    if (a%k==0 && b%k==0) {
        cout<<"Both\n";
    } else if (a%k==0) {
        cout<<"Memo\n";
    } else if (b%k==0) {
        cout<<"Momo\n";
    } else {
        cout<<"No One\n";
    }
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