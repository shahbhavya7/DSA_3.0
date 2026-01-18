#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums){
        int cnt1=0,cnt2=0,cnt3=0;
        int n=nums.size();
        for(auto num:nums){
            if(num==0) cnt1++;
            else if(num==1) cnt2++;
            else cnt3++;
        }
        int index=0;
        while(cnt1--){
            nums[index]=0;
            index++;
        }
        while(cnt2--){
            nums[index]=1;
            index++;
        }
        while(cnt3--){
            nums[index]=2;
            index++;
        }
    }

    void sortColorsOptimized(vector<int>& nums){
        int n=nums.size();
        int low=0, mid=0, high = n-1;
        while(mid<=high){
            if(nums[mid]==0){
                swap(nums[low], nums[mid]);
                low++;
                mid++;
            }
            else if(nums[mid]==1){
                mid++;
            }
            else{
                swap(nums[mid], nums[high]);
                high--;
            }
        }
    }
};

int main(){
    Solution sol;
    vector<int> nums = {2, 0, 2, 1, 1, 0};
    sol.sortColors(nums);
    for(int num : nums){
        cout << num << " ";
    }
    cout << endl;
    vector<int> numsOpt = {2, 0, 2, 1, 1, 0};;
    sol.sortColorsOptimized(numsOpt);
    for(int num : numsOpt){
        cout << num << " ";
    }
    
    return 0;
}