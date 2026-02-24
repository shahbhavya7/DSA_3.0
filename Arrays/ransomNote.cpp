#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> hash(26, 0);
        for (char c : magazine) {
            hash[c - 'a']++;
        }
        for (char c : ransomNote) {
            if (hash[c - 'a'] == 0) {
                return false;
            }
            hash[c - 'a']--;
        }
        return true;
    }
};

int main(){
    Solution sol;
    string ransomNote = "a";
    string magazine = "b";
    cout << sol.canConstruct(ransomNote, magazine) << endl;
    return 0;
}