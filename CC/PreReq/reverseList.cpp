#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    vector<int> reversed_arr(n);
    for (int i = 0; i < n; i++) {
        reversed_arr[i] = arr[n - 1 - i];
    }
    for (int i = 0; i < n; i++) {
        cout << reversed_arr[i] << " ";
    }
    return 0;
}