// https://leetcode.com/problems/maximum-width-of-binary-tree/description/


// DFS, TC:(N), SC:O(W)
class Solution {

public:
    vector<unsigned long long> memo;
    int dfs(TreeNode* root, int depth, unsigned long long i) {
        if (!root) return 0;
        if (memo.size() < depth + 1) {
            memo.push_back(i);
        }
        unsigned long long res = max(dfs(root->left, depth+1, 2*i+1), dfs(root->right, depth+1, 2*i+2));
        return max(i - memo[depth]+1, res);
    }

    int widthOfBinaryTree(TreeNode* root) {
        return dfs(root, 0, 0);
    }
};


// BFS, TC:(N), SC:O(W)
class Solution2 {

public:
    int widthOfBinaryTree(TreeNode* root) {
        unsigned long long res = 1;
        queue<pair<TreeNode*, unsigned long long>> q;
        q.push(pair<TreeNode*, unsigned long long> (root, 0));
        while (!q.empty()) {
            int n = q.size();
            for (int i=0; i<n; i++) {
                pair<TreeNode*, unsigned long long> p = q.front();
                q.pop();
                if (p.first->left)
                    q.push(pair<TreeNode*, unsigned long long> (p.first->left, 2*p.second+1));
                if (p.first->right)
                    q.push(pair<TreeNode*, unsigned long long> (p.first->right, 2*p.second+2));

            }
            if (!q.empty()) {
                // cout<<"rightmost "<<q.back().second<<"\n";
                // cout<<"leftmost "<<q.front().second<<"\n";
                // cout<<"res "<<res<<"\n";
                res = max(res, q.back().second - q.front().second + 1);
            }

        }
        return res;


    }
};