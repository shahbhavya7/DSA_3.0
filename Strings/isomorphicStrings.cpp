#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char,int> m1,m2;
        int n=s.size();
        for (int i = 0; i < n; i++) {
            m1[s[i]] = i+1; // we store the index + 1 to avoid confusion with default value 0 for characters not seen before
            m2[t[i]] = i+1;
        }
        for (int i = 0; i < n; i++) {
            if (m1[s[i]] != m2[t[i]]) { // if the last seen indices of the characters do not match, they are not isomorphic
                return false;
            }
        }
        return true; // if we successfully check all characters, the strings are isomorphic
    }

    bool isIsomorphicOptim(string s, string t){
        int m1[256]={0},m2[256]={0}; // using arrays to store the last seen indices of characters, assuming ASCII character set
        int n=s.size();
        for (int i = 0; i < n; i++) {
            if (m1[s[i]] != m2[t[i]]) { // if the last seen indices of the characters do not match, they are not isomorphic
                return false;
            }
            m1[s[i]] = i+1; // we store the index + 1 to avoid confusion with default value 0 for characters not seen before
            m2[t[i]] = i+1;
        }
        return true; // if we successfully check all characters, the strings are isomorphic
    }
};

int main(){
    Solution sol;
    string s,t;
    s = "egg";
    t = "add";
    cout<<sol.isIsomorphic(s,t)<<endl;
    return 0;
}