#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char,string> m1; // map to store the mapping from pattern characters to words
        unordered_map<string,char> m2; // map to store the mapping from words to pattern
        istringstream iss(s); // use istringstream to split the string s into words
        string word;
        for (char c : pattern) { // iterate through each character in the pattern
            if (!(iss >> word)) { // if we cannot read a word for the current pattern character, return false
                return false;
            }
            if (m1.count(c) && m1[c] != word) { 
                // if there is already a mapping for the current pattern character and it does not match the current word, return false
                // m1.count(c) checks if there is a mapping for character c, and m1[c] != word checks if the mapped word does not match the current word
                return false;
            }
            if (m2.count(word) && m2[word] != c) { // if there is already a mapping for the current word and it does not match the current pattern character, return false
                return false;
            }
            // we use two maps to ensure that the mapping is consistent in both directions (pattern to word and word to pattern)
            // if we only used one map, we could have a situation where two different pattern characters map to the same word, which would not be correct
            m1[c] = word; // create/update the mapping from pattern character to word
            m2[word] = c; // create/update the mapping from word to pattern character
        }
        if (iss >> word) { // if there are still words left in the string after processing the pattern, return false
            return false;
        }
        return true; // if we successfully process the entire pattern and string, return true
    }
};

int main(){
    Solution sol;
    string pattern, s;
    pattern = "abba";
    s = "dog cat cat dog";
    cout<<sol.wordPattern(pattern,s)<<endl;
    if(sol.wordPattern(pattern,s)){
        cout<<"The string follows the pattern."<<endl;
    } else {
        cout<<"The string does not follow the pattern."<<endl;
    }
    return 0;
}