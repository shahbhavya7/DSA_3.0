#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    int a,b;
    char op;
    cin >> a >> op >> b;
    if(a>b && op == '>')
        cout << "Right" << endl;
    else if(a<b && op == '<')
        cout << "Right" << endl;
    else if(a==b && op == '=')
        cout << "Right" << endl;
    else
        cout << "Wrong" << endl;
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