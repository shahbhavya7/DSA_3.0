#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    float a, b;
    cin >> a >> b;
    float div = a / b;
    // round of to nearest integer
    int roundd = round(div);
    // floor of the division
    int floorr = floor(div);
    // ceil of the division
    int ceill = ceil(div);
    cout << "floor "<<a<<" / "<<b<<" = "<<floorr<<endl;
    cout << "ceil "<<a<<" / "<<b<<" = "<<ceill<<endl;
    cout << "round "<<a<<" / "<<b<<" = "<<roundd<<endl;

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