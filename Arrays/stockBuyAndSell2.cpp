#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int maxProfit = 0;
        int j = 0;
        int k = 1;
        while(k < n){
            if(prices[k] > prices[j]){
                maxProfit += prices[k] - prices[j];
                j++;
                k++;
            }
            else{
                j++;
                k++;
            }
        }
        return maxProfit;
    }
};

int main(){
    Solution sol;
    vector<int> prices = {1,2,3,4,5};
    int profit = sol.maxProfit(prices);
    cout << "Maximum Profit: " << profit << endl;

    return 0;
}