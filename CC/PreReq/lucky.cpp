#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >> n;
    while (n >= 10) // Loop as long as n is a two-digit number or more
    {
        int sum = 0;
        while (n > 0)
        {
            sum += n % 10;
            n /= 10;
        }
        n = sum; // Update n to be the sum, so we can check if it is still >= 10
    }
    if(n==9) cout << "Lucky" << endl;
    else cout << "Not Lucky" << endl;

    return 0;
}
