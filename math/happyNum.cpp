#include <bits/stdc++.h>
using namespace std;

class SolutionBrute
{
public:
    bool isHappy(int n)
    {
        if (n == 1 || n == 7)
            return true; // 1 and 7 are happy numbers
        if (n < 10)
            return false; // Single digit numbers other than 1 and 7 are not happy

        int sum = 0;
        while (n > 0)
        {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        return isHappy(sum); // Recursive call with the sum of squares of digits
    }
};

class Solution
{
public:
    bool isHappy(int n)
    {
        int slow = getNextNumber(n);
        int fast = getNextNumber(getNextNumber(n));

        while (slow != fast)
        {
            if (fast == 1)
                return true;
            slow = getNextNumber(slow);
            fast = getNextNumber(getNextNumber(fast));
        }

        return slow == 1; // return true if the slow pointer is at 1, otherwise return false (cycle detected)
    }

    int getNextNumber(int n)
    {
        int output = 0;

        while (n > 0)
        {
            int digit = n % 10;
            output += digit * digit;
            n = n / 10;
        }

        return output;
    }
};

int main()
{
    Solution sol;
    int n = 19;
    cout << sol.isHappy(n) << endl; // Output: 1 (true)
    return 0;
}