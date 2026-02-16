#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cout << "Enter a number: ";
    cin >> n;
    int sum = 0;
    // finding the number of digits in the number
    int temp = n;
    int digits = 0;
    while (temp > 0)
    {
        temp /= 10;
        digits++;
    }
    // finding the sum of the digits raised to the power of the number of digits
    temp = n;
    while (temp > 0)
    {
        int digit = temp % 10; 
        sum += round(pow(digit, digits));
        temp /= 10;
    }
    // checking if the sum is equal to the original number
    if (sum == n)
    {
        cout<< "Armstrong" << endl;
    }
    else
    {
        cout << "Not Armstrong" << endl;
    }
    return 0;
}