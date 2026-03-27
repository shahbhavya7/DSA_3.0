#include <bits/stdc++.h>
using namespace std;

class SolutionBrute
{
public:
    string toBinary(int n)
    {
        string res = "";
        while (n > 0)
        {
            res = to_string(n % 2) + res;
            n /= 2;
        }
        return res;
    }

    int hammingWeight(int n)
    {
        string binary = toBinary(n);
        int count = 0;
        for (char c : binary)
        {
            if (c == '1')
                count++;
        }
        return count;
    }
};

class Solution
{
public:
    int hammingWeight(int n)
    {
        int cnt = 0;
        while(n > 0){
            if (n % 2 == 1) // Check if the least significant bit is 1
                cnt++;
            n /= 2; // Right shift the bits by dividing by 2
        }
        return cnt;
    }
};

int main()
{
    Solution sol;
    int n = 11;                           // Example input
    cout << sol.hammingWeight(n) << endl; // Output: 3 (since 11 in binary is 1011 which has three '1's)
    return 0;
}