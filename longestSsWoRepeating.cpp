#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        int n = s.size();
        int maxLen = 0;
        for (int i = 0; i < n; i++)
        {
            vector<int> hash(256, 0); // to store frequency of characters
            for (int j = i; j < n; j++)
            {
                if (hash[s[j]] == 1) 
                    break;
                hash[s[j]] = 1;          // mark character as seen
                int currLen = j - i + 1; // +1 because both i and j are inclusive i.e i and j are part of the substring
                maxLen = max(maxLen, currLen);
            }
        }
        return maxLen;
    }
    int lengthOfLongestSubstringOptimal(string s)
    {
        int n = s.size();
        int maxLen = 0;
        vector<int> hash(256, -1); // Store the LAST index of each character
        int left = 0, right = 0;
        while (right < n)
        {
            if (hash[s[right]] != -1)
            {
                left = max(hash[s[right]] + 1, left); // Move the left pointer to the right of the last occurrence of s[right]
            }
            int currlen = right - left + 1;
            maxLen = max(maxLen, currlen);
            hash[s[right]] = right; // Update the last index of s[right]
            right++;
        }
        return maxLen;
    }
};

int main()
{
    Solution sol;
    string s = "abcabcbb";
    int result = sol.lengthOfLongestSubstringOptimal(s);
    cout << "Length of Longest Substring Without Repeating Characters: " << result << endl;
    return 0;
}