#include <bits/stdc++.h>
using namespace std;

string toBinary(int n)
{
    string res = "";
    while (n > 0)
    {
        res = to_string(n % 2) + res; // for binary representation, we take the remainder when n is divided by 2
        n /= 2;
    }
    return res;
}

string toBinaryEfficient(int n)
{
    if (n == 0)
        return "0"; // Handle the zero edge case

    // Optional: Handle negative numbers by converting to positive
    // and prepending a '-' sign later, if that fits your use case.
    bool isNegative = n < 0;
    unsigned int num = abs(n);

    string res = "";
    while (num > 0)
    {
        // Append characters directly (much faster than to_string)
        res += (num % 2 == 0 ? '0' : '1'); // divide by 2 and check the remainder, if it's 0, append '0', else append '1' to the result string
        num /= 2;
    }

    // Reverse the string at the end as we built it in reverse order
    reverse(res.begin(), res.end());

    return (isNegative ? "-" : "") + res; // Prepend '-' if the original number was negative
}

int main()
{
    int n;
    cin >> n;
    cout << toBinary(n) << endl;
    cout << toBinaryEfficient(n) << endl;
    return 0;
}