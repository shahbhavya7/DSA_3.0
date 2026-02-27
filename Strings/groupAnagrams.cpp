#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        for (string s : strs) { 
            string t = s; 
            sort(t.begin(), t.end());
            mp[t].push_back(s); // for each string we sort it and use the sorted string as a key in the map and push the original string into the vector of that key. This way all anagrams will be grouped together under the same sorted key.
            // this sorted string will be same for all anagrams and different for non-anagrams. So all anagrams will be grouped together in the map under the same key.
        }
        vector<vector<string>> anagrams;
        for (auto p : mp) { 
            anagrams.push_back(p.second);
        }
        return anagrams;
    }
};

int main(){
    Solution sol;
    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
    vector<vector<string>> result = sol.groupAnagrams(strs);
    for (const auto& group : result) {
        for (const auto& word : group) {
            cout << word << " ";
        }
        cout << endl;
    }
    
    return 0;
}