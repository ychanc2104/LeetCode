// https://leetcode.com/problems/path-sum-ii/description/


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

// dfs, TC:O(N^2), SC:O(N)
class Solution {
public:
    vector<int> path;
    vector<vector<int>> res;

    void dfs(TreeNode* root, int targetSum) {
        if (!root) return;
        if (!root->left && !root->right && targetSum==root->val) {
            path.push_back(root->val);
            vector<int> path_new;
            for (int num: path) path_new.push_back(num);
            path.pop_back();
            res.push_back(path_new);
        }
        path.push_back(root->val);
        dfs(root->left, targetSum - root->val);
        dfs(root->right, targetSum - root->val);
        path.pop_back();
    }
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        dfs(root, targetSum);
        return res;
    }
};