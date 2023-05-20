// https://leetcode.com/problems/profitable-schemes/description/


//
class Solution {
public:
    int dp[101][101][101];
    int mod=1e9 + 7;
    int helper(int i, int n, int minProfit, vector<int>& group, vector<int>& profit) {

        if (i==group.size()) return 0;
        if (dp[i][n][minProfit] != -1) return dp[i][n][minProfit];
        int res = helper(i+1, n, minProfit, group, profit);
        if (n >= group[i]) {
            res += helper(i+1, n-group[i], max(0, minProfit-profit[i]), group, profit);
            if (profit[i] >= minProfit) {
                res++;
            }
        }
        dp[i][n][minProfit] = res % mod;
        return dp[i][n][minProfit];

    }
    int profitableSchemes(int n, int minProfit, vector<int>& group, vector<int>& profit) {
        memset(dp, -1, sizeof(dp));
        return helper(0, n, minProfit, group, profit) + (minProfit==0);
    }
};