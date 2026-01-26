#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int n = prices.size();
        int maxProfit = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                int profit = prices[j] - prices[i];
                maxProfit = max(maxProfit, profit);
            }
        }
        return maxProfit;
    }

    int maxProfitOptimized(vector<int> &prices)
    {
        int n = prices.size();
        int minPrice = INT_MAX;
        int maxProfit = 0;
        for (auto price : prices)
        {
            if (price < minPrice)
            {
                minPrice = price;
            }
            else
            {
                maxProfit = max(maxProfit, price - minPrice);
            }
        }
        return maxProfit;
    }
};

int main()
{
    Solution sol;
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    int result = sol.maxProfit(prices);
    cout << "Maximum Profit: " << result << endl;
    int resultOpt = sol.maxProfitOptimized(prices);
    cout << "Maximum Profit (Optimized): " << resultOpt << endl;
    return 0;
}