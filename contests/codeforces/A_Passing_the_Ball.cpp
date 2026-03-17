#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve() {
    int n;
    string s;
    cin >> n >> s;
    vector<int> arr(50, 0); // max students can be 50 
    int students = 0;
    arr[0] = 1; // first student always gets the ball
    students++;
    int j = 0; // index for arr
    for (int i = 0; i < n; i++) {
        if(s[j]=='R'){
            j++;
            if(arr[j]==0) {
                arr[j] = 1;
                students++;
            }
        }
        else if(s[j]=='L') {
            j--;
    }
}
    cout << students << "\n";
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

