#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    ll x;
    cin >> x;
    ll n = x;
    ll sum = 0;
    vector<int> digits;
    while (n > 0) {
        int current_digit = n % 10;
        sum += current_digit;
        n /= 10;
        if (n == 0) {
            // If n is now 0, current_digit was the leading digit.
            // It can only be reduced to 1 (e.g., a 6 reduces by 5).
            digits.pb(current_digit - 1);
        } else {
            // All other digits can be reduced to 0.
            digits.pb(current_digit);
        }
    }
    ll moves = 0;
    if(sum <= 9) {
        cout << moves << "\n";
        return;
    }
    ll extra = sum - 9;
    sort(digits.rbegin(), digits.rend()); // sort in descending order to remove largest digits first
    int idx = 0;
    while(sum > 9){
        int dig  = digits[idx]; // get the last digit of the current number
        if(dig == 0){
            idx++;
            continue;
        }
        else {
            sum -= dig;
            moves++;
            idx++;
        }
    }
    cout << moves << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}