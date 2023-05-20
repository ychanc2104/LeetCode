// https://leetcode.com/problems/path-sum-iii/description/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
// prefix sum + dfs, TC:O(N), SC:O(N)
class Solution {
public:
    int res;
    int target;
    unordered_map<long long, int> memo = {{0, 1}};
    void dfs(TreeNode* root, long long s) {

        if (!root) return;
        s += root->val;
        if (memo.find(s - target) != memo.end()) {
            // found
            res += memo[s - target];
        }

        memo[s]++;
        dfs(root->left, s);
        dfs(root->right, s);
        memo[s]--; // can only go down
    }

    int pathSum(TreeNode* root, int targetSum) {
        target = targetSum;
        dfs(root, 0);
        return res;
    }
};