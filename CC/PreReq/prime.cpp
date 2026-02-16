#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    if(n <= 1){
        cout << "NOT Prime" << endl;
        return 0;
    }
    for (int i = 2; i < n; i++) {
        if(n % i == 0){
            cout << "NOT Prime" << endl;
            return 0;
        }
    }
    cout << "Prime" << endl;
    return 0;
}