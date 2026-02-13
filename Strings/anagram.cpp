#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isAnagramBetter(string s, string t) {
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return s == t;
    }
    bool isAnagram(string s, string t){
        if (s.length() != t.length()) return false;
        vector<int> count(26, 0);
        for (int i = 0; i < s.length(); i++) {
            count[s[i] - 'a']++; // Increment count for characters in s
            count[t[i] - 'a']--; // Decrement count for same characters in t
            // If in s we have 'a' then count for its ascii index will be incremented
            // If in t we have 'n' then count for its ascii index will be decremented
            // when 'a' again comes in t then count for its ascii index will be decremented again and it will become 0
            // same for 'n' when it comes in s then count for its ascii index will be incremented again and it will become 0
            // This way we can check if the count of all characters is 0 at the end then they are anagrams otherwise not
        }
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) return false;
        }
        return true;
    }

};

int main(){
    Solution sol;
    string s = "anagram";
    string t = "nagaram";
    if(sol.isAnagram(s, t)){
        cout << "The strings are anagrams." << endl;
    } else {
        cout << "The strings are not anagrams." << endl;
    }
    return 0;
}