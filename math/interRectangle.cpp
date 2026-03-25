#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long interchangeableRectangles(vector<vector<int>>& rectangles) {
        unordered_map<double, long long> ratioCount; // Map to count occurrences of each ratio
        long long count = 0; // To store the total count of interchangeable pairs
        for (auto it : rectangles){
            double ratio = (double)it[0] / it[1]; // Calculate the ratio of width to height
            count += ratioCount[ratio]; // Add the count of previously seen rectangles with the same ratio
            ratioCount[ratio]++; // Increment the count for this ratio
        }
        return count; // Return the total count of interchangeable pairs
    }
};

int main(){
    Solution sol;
    vector<vector<int>> rectangles = {{4, 8}, {3, 6}, {10, 20}, {5, 10}};
    cout << sol.interchangeableRectangles(rectangles) << endl; // Output: 6 (since all rectangles have the same ratio of 0.5, they are all interchangeable)
    return 0;
}