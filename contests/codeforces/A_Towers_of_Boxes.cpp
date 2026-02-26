#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    int n, m , d;
    cin >> n >> m >> d;
    int towers = 0;
    int load = 0;
    bool base = false;
    for (int i = 0; i < n; i++) {
        if(load <= d){
            if(base==false){
                towers++;
                base = true;
                load = load + m;
            }
            else load = load + m;
        }
        else {
            load = 0;
            base = false;
            i--;
        }
    }
    cout << towers << "\n";
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