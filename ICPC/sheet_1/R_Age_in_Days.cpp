#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    int age;
    cin >> age;
    int years = age / 365;
    int remaining_days = age % 365;
    int months = remaining_days / 30;
    int days = remaining_days % 30;
    cout << years << " years"<<endl;
    cout << months << " months"<<endl;
    cout << days << " days"<<endl;
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