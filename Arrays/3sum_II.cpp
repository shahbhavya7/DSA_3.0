#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> res(2);
        int n = numbers.size();
        int left = 0, right = n - 1;
        while(left < right){
            int sum  = numbers[left] + numbers[right];
            if(sum == target){
                res[0] = left + 1; // +1 because the problem might be using 1-based indexing
                res[1] = right + 1;
                return res;
            }
            else if(sum < target){
                left++;
            }
            else{
                right--;
            }
        }
        return res;
    }
};

int main(){
    Solution sol;
    vector<int> numbers = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = sol.twoSum(numbers, target);
    for(int index : result){
        cout << index << " ";
    }
    return 0;
}