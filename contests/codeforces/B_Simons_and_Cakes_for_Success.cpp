#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back
constexpr long long MOD = 1e9+7;

#include <iostream>
using namespace std;

void solve() {
    long long n;
    cin >> n;

    long long temp = n;
    long long k = 1;

    for (long long i = 2; i * i <= temp; i++) { 
        if (temp % i == 0) {
            k *= i;                 
            while (temp % i == 0)
                temp /= i;          
        }
    }

    if (temp > 1)
        k *= temp;

    cout << k << "\n";
}

int main() {
    int t;
    cin >> t;
    while (t--)
        solve();
}

