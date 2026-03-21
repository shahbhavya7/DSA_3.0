#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    bool isThree(int n)
    {
        if (n < 2)
            return false;
        int cnt = 2; // 1 and n are always divisors for n >= 2
        for (int i = 2; i * i <= n; i++)
        {
            if (n % i == 0)
            {
                cnt++;
                if (i != n / i)
                    cnt++;
                if (cnt > 3)
                    return false;
            }
        }
        return cnt == 3;
    }
};

int main()
{
    Solution sol;
    int n = 4;
    bool result = sol.isThree(n);
    cout << (result ? "true" : "false") << endl; // if result is true, print "true", otherwise print "false"
    return 0;
}