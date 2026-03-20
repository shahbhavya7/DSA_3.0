#include <bits/stdc++.h>
using namespace std;

class SolutionRecursive
{
public:
    double power(double x, long long n)
    {
        if (n == 0)
            return 1.0;
        if (n == 1)
            return x;
        if (n % 2 == 0)
        {  // if n is even
            return myPow(x * x, n / 2); // multiply x twice and reduce n to half
        }
        else
        {
            return x * myPow(x, n - 1); // reduce n by 1 and multiply x once
        }
    }
    double myPow(double x, int n)
    {
        long long num = n; // converting to long long to avoid overflow for -2^31
        if (num < 0)
        {
            return (1.0 / power(x,-1 * num));
        }
        return power(x, num);
    }
};

class SolutionIterative
{
public:
    double myPow(double x, int n)
    {
        long long num = n; // converting to long long to avoid overflow for -2^31
        if (num < 0) // if n is negative, we can take the reciprocal of x and make n positive to simplify 
        // the calculation
        {
            x = 1 / x;
            num = -num;
        }
        double result = 1.0;
        while (num > 0)
        {
            if (num % 2 == 1) // if n is odd, we can multiply the result by x and reduce n by 1 to make it even
            {
                result = result * x;
                num--;
            }
            else // if n is even, we can multiply x by itself and reduce n to half to optimize the calculation
            {
                x *= x;
                num /= 2;
            }
        }
        return result;
    }
};

int main()
{

    SolutionIterative sol;
    double x = 2.00000;
    int n = 20;
    double result = sol.myPow(x, n);
    cout << "Result: " << result << endl;

    return 0;
}