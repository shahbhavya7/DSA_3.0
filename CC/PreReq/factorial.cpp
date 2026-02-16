#include<bits/stdc++.h>
using namespace std;
int main(){
    // factorial digits
    int n;
    cin >> n;
    int fact = 1;
    for (int i = 1; i <= n; i++) {
        fact *= i;
    }
    int sum = 0;
    while (fact > 0) {
        sum += fact % 10;
        fact /= 10;
    }
    cout << sum << endl;
    return 0;
}