#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    float x, y;
    cin >> x >> y;
    if (x > 0 && y > 0) {
        cout << "Q1" << endl;
    } else if (x < 0 && y > 0) {
        cout << "Q2" << endl;
    } else if (x < 0 && y < 0) {
        cout << "Q3" << endl;
    } else if (x > 0 && y < 0) {
        cout << "Q4" << endl;
    } else if (x == 0 && y == 0) {
        cout << "Origem" << endl;
    } else if (x == 0) {
        cout << "Eixo Y" << endl;
    } else if (y == 0) {
        cout << "Eixo X" << endl;
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