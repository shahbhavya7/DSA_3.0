#include<bits/stdc++.h>
using namespace std;

void fibonacci(int n){ // Function to print the first n Fibonacci numbers
    int a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        cout << a << " ";
        int next = a + b;
        a = b;
        b = next;
    }
    cout << endl;
}

int main(){
    int n;
    cin >> n;
    fibonacci(n);
    return 0;
}