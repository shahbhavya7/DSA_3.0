#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        if (strs.empty())
            return "";
        sort(strs.begin(), strs.end());
        string first = strs[0];
        string last = strs.back();

        string prefix = "";
        int n = min(first.size(), last.size());
        for (int i = 0; i < n; i++)
        {
            if (first[i] != last[i])
                break;
            prefix += first[i];
        }
        return prefix;
    }
};

int main()
{
    Solution sol;
    vector<string> strs = {"flower", "flow", "flight"};
    string lcp = sol.longestCommonPrefix(strs);
    cout << "Longest Common Prefix: " << lcp << endl;
    return 0;
}