#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    string reverseWords(string s)
    { // using stringstream
        stringstream ss(s);
        string word;
        vector<string> words;
        int n = s.size();
        while (ss >> word)
        { // extract words from the stringstream into 'word'
            words.push_back(word);
        }
        reverse(words.begin(), words.end()); // reverse the vector of words
        string result;
        int m = words.size();
        for (int i = 0; i < m; i++)
        {
            result += words[i];
            if (i != m - 1)
                result += " "; // if not the last word, add a space
        }
        return result;
    }

    string reverseWordsOptimal(string s){
        int n = s.length();
        string result = "";

        reverse(s.begin(), s.end()); // reverse the entire string

        for (int i = 0; i < n; i++) {
            string word = "";
            while(i<n && s[i]!=' '){
                word += s[i];
                i++;
            }
            reverse(word.begin(), word.end()); // reverse the individual word
            if(word.length() > 0) result += " " + word; // add the word to result with a space
        }
        return result.substr(1) ; // remove the trailing space at the beginning
    }
};

int main()
{
    Solution sol;
    string s = "the sky is blue";
    string result = sol.reverseWordsOptimal(s);
    cout << "Reversed Words: " << result << endl;

    return 0;
}