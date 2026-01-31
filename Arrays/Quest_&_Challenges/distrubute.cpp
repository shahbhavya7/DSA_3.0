#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int distMoney(int m, int c)
    {
        int val = m - c; // initial distribution of 1 dollar to each child
        int count = 0;
        if (val < 0) // not enough money to give each child at least 1 dollar then return -1
            return -1;
        else
        {
            if (val < 7) // if after giving 1 dollar to each child less than 7 dollars are left then no child can get 8 dollars
                return 0; 
            else
            {
                count = val / 7; // maximum children who can get 8 dollars
                int rem = val % 7; // these many dollars left after giving 8 dollars exact to 1,2 .. children
                if (rem == 3 && count == c - 1) // as we dont want any child to have exactly 4 dollars so if 3 dollars are left and all 
                // other children have 8 dollars then we need to reduce one child having 8 dollars to avoid having a child with exactly 4 dollars
                    count--;
                if (count == c && rem > 0) // if all children are having 8 dollars and some money is still left then we need to reduce one child having 
                //8 dollars as we need to distribute all money so that some child can have more than 8 dollars
                    count--;
                if (count > c) // If all c children are given 8 dollars but some money remains,
                // that extra money must go to someone and can force a child to end up with 4 dollars (invalid case).
                // Hence we reduce one 8-dollar child and return c-1, thats the maximum valid children with 8 dollars (greedy approach).
                    return c - 1;
                return count;
            }
        }
    }
};

int main()
{
    Solution sol;
    int money = 20;
    int children = 3;
    int result = sol.distMoney(money, children);
    cout << "Maximum children with 8 dollars: " << result << endl;
    return 0;
}