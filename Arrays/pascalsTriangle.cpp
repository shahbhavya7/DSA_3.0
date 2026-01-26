#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> triangle;
        for(int i=0; i<numRows;i++){
            vector<int> row(i+1,1); // this vector will have i+1 elements all initialized to 1
            for(int j=1;j<i;j++){
                row[j] = triangle[i-1][j-1] + triangle[i-1][j];
            }
            triangle.push_back(row);
        }
        return triangle;
    }
};

class SolutionOptimized { // generate only Nth row using combinatorial formula
public:
    vector<long long> getNthRow(int N) {
        vector<long long> row;
        
        // First value of the row is always 1
        long long val = 1;
        row.push_back(val);
        
        // C(n, k) = C(n, k-1) * (n-k) / k
        for (int k = 1; k < N; k++) {
            val = val * (N - k) / k;
            row.push_back(val);
        }
        
        return row;
    }
};

int main(){
    Solution sol;
    int numRows = 5; // Example input
    vector<vector<int>> result = sol.generate(numRows);
    for(const auto& row : result){
        for(int val : row){
            cout << val << " ";
        }
        cout << endl;
    }

    SolutionOptimized solOpt;
    int N = 5; // Example input for Nth row
    vector<long long> nthRow = solOpt.getNthRow(N);
    for(long long val : nthRow){
        cout << val << " ";
    }
    cout << endl;

    return 0;
}