#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    bool hasAlternatingBits(int n)
    {
        while (n > 0) // Loop until all bits are processed
        {
            int curr = n % 2; // Get the last bit
            n = n / 2;        // Move to the next bit
            int next = n % 2; // Get the new last bit

            if (n > 0 && curr == next)
            {
                return false;
            }
        }
        return true;
    }
};

int main()
{
    Solution sol;
    int n = 7;
    bool result = sol.hasAlternatingBits(n);
    cout << "Has Alternating Bits: " << (result ? "Yes" : "No") << endl;
    return 0;
}