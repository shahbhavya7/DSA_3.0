#include <bits/stdc++.h>
using namespace std;
class Solution
{ 
public:

    bool findRotation(vector<vector<int>>& mat, vector<vector<int>>& target) {
        rotateMat(mat);
        if(mat!=target){
            rotateMat(mat);
            if(mat!=target){
                rotateMat(mat);
                if(mat!=target){
                    rotateMat(mat);
                    if(mat!=target){
                        return false;
                    }
                }
            }
        }
        return true;
    }

    void rotateMat(vector<vector<int>>& matrix){
        int n  = matrix.size();
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
        for (int i = 0; i < n; i++) {
            reverse(matrix[i].begin(),matrix[i].end());
        }
    }
};


int main()
{   
    Solution sol;
    vector<vector<int>> mat = { 
        // {5, 1, 9, 11},
        // {2, 4, 8, 10},
        // {13, 3, 6, 7},
        // {15, 14, 12, 16}
        {0,0,0},
        {0,1,0},
        {1,1,1}
    };
    vector<vector<int>> target = {
        // {15, 13, 2, 5},
        // {14, 3, 4, 1},
        // {12, 6, 8, 9},
        // {16, 7, 10, 11}
        {1,1,1},
        {0,1,0},
        {0,0,0}
    };
    bool result = sol.findRotation(mat, target);
    cout << (result ? "true" : "false") << endl;
    return 0;
}