#include<bits/stdc++.h>
using namespace std;
int main(){
    string s = "abcabcbb";
    vector<int> mpp(256, 0);
    for(int i=0; i<s.size(); i++){
        mpp[s[i]]++; // s[i] is character at index i, it converts to its ASCII value when used as index in vector
    }
    // printing frequency of each character
    for(int i=0; i<256; i++){
        if(mpp[i] > 0){
            cout << char(i) << " : " << mpp[i] << endl;
        }
    } 
    return 0;
}