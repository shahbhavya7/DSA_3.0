#include<bits/stdc++.h>
using namespace std;

int toDecimal(string s){
    int res=0;
    for(int i=0;i<s.size();i++){
        res=res*2+(s[i]-'0'); // for decimal representation, we multiply the result by 2 and add the current digit (converted from character to integer)
    }
    return res;
}

int main(){
    string s;
    cin>>s;
    cout<<toDecimal(s)<<endl;
    return 0;
}