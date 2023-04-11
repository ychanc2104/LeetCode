// https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/


// dfs, TC:O(N+M), SC:O(N+M)
class Solution {
public:

    int dfs(int node, unordered_map<int, vector<int>>& graph, string& colors, vector<vector<int>>& counter, vector<int>& visited, vector<int>& inPath) {
        if (inPath[node]) return INT_MAX;
        if (visited[node]) return counter[node][colors[node] - 'a'];
        inPath[node] = 1;
        visited[node] = 1;
        for (auto& nei : graph[node]) {
            if (dfs(nei, graph, colors, counter, visited, inPath) == INT_MAX) return INT_MAX;
            // update counter
            for (int i=0; i<26; i++) {
                counter[node][i] = max(counter[node][i], counter[nei][i]);
            }
        }
        counter[node][colors[node] - 'a']++;
        inPath[node] = 0;
        return counter[node][colors[node] - 'a'];
    }
    int largestPathValue(string colors, vector<vector<int>>& edges) {
        int n = colors.size();
        unordered_map<int, vector<int>> graph;
        vector<vector<int>> counter(n, vector<int>(26));
        vector<int> visited(n);
        vector<int> inPath(n);

        for (int i=0; i<edges.size(); i++) {
            graph[edges[i][0]].push_back(edges[i][1]);
        }
        int res = 0;
        for (int i=0; i<n; i++) {
            // must exist global max if iterate all node
            res = max(res, dfs(i, graph, colors, counter, visited, inPath));
        }
        return res==INT_MAX ? -1 : res;


    }
};