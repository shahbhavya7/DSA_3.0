#include<bits/stdc++.h>
using namespace std;

class Solution {
    public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) { 
        sort(intervals.begin(),intervals.end()); // sort based on first element of each vector
        vector<vector<int>> merged; // to store merged intervals
        for(auto interval : intervals){ // traverse each interval
            if(merged.empty() || merged.back()[1] < interval[0]){ // if merged is empty or no overlap, merge.back()[1] gives last element of last vector in merged list
                merged.push_back(interval); // interval[0] is first element of current vector in intervals list
            }
            else{ // overlap exists
                merged.back()[1] = max(merged.back()[1],interval[1]); // if overlap then last element of last vector in merged list is updated 
                // to max of last element of last vector in merged list and last element of current vector in intervals list
                // like if merged = [[1,3]] and current interval = [2,6], then merged.back()[1] = max(3,6) = 6 and merged becomes [[1,6]] 
            }
        }
        return merged;
    }
};

int main(){
    Solution sol; 
    vector<vector<int>> intervals = {
        {1,3},
        {2,6},
        {8,10},
        {15,18}
    };
    vector<vector<int>> merged = sol.merge(intervals);
    for (const auto& interval : merged) {
        cout << "[" << interval[0] << ", " << interval[1] << "] ";
    }

    return 0;
}