#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    string categorizeBox(int length, int width, int height, int mass)
    {
        bool bulky = false;
        bool heavy = false;
        long long volume = (long long)length * width * height;
        if (length >= pow(10, 4) || width >= pow(10, 4) || height >= pow(10, 4) || volume >= pow(10, 9))
        {
            bulky = true;
        }
        if (mass >= 100)
        {
            heavy = true;
        }
        if (bulky && heavy)
            return "Both";
        else if (bulky)
            return "Bulky";
        else if (heavy)
            return "Heavy";
        else
            return "Neither";
    }
};

int main()
{
    Solution sol;
    int length = 1000;
    int width = 35;
    int height = 700;
    int mass = 300;
    string result = sol.categorizeBox(length, width, height, mass);
    cout << "Category of the box: " << result << endl;
    return 0;
}