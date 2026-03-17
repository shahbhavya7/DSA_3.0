#include<bits/stdc++.h>
using namespace std;

int binarySearch(vector<int>&nums,int target){
    int low = 0;
    int high = nums.size()-1;
    while(low<=high){
        int mid  = low + (high-low)/2; // To avoid potential overflow we use this formula instead of (low+high)/2
        if(nums[mid] == target) return mid;
        else if(nums[mid] < target) low = mid+1;
        else high = mid-1;
    }
    return 0; // if target is not found, return 0 (or you can return low if you want the insert position)
}

int main(){
    vector<int> nums = {1,3,5,6};
    int target = 2;
    cout << binarySearch(nums,target) << "\n"; // Output: 2
    return 0;
}