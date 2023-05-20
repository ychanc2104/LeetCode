# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description/


class Solution {
public:
    int find(vector<int>& parents, int x) {
        if (x != parents[x]) {
            parents[x] = find(parents, parents[x]);
        }
        return parents[x];
    }

    void unionx(vector<int>& parents, int x, int y) {
        int px = find(parents, x);
        int py = find(parents, y);
        parents[px] = py;
    }

    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        vector<int> parents_a(n);
        vector<int> parents_b(n);
        for (int i=0; i<n; i++) {
            parents_a[i] = i;
            parents_b[i] = i;
        }
        int res = 0;
        for (auto edge: edges) {
            if (edge[0]==3) {
                bool check = (find(parents_a, edge[1]-1) == find(parents_a, edge[2]-1)) && (find(parents_b, edge[1]-1) == find(parents_b, edge[2]-1));
                if (check) {
                    res++;
                }

                unionx(parents_a, edge[1]-1, edge[2]-1);
                unionx(parents_b, edge[1]-1, edge[2]-1);
            }
        }
        for (auto edge: edges) {
            if (edge[0]==1) {
                if (find(parents_a, edge[1]-1) == find(parents_a, edge[2]-1)) {
                    res++;
                }
                unionx(parents_a, edge[1]-1, edge[2]-1);
            } else if (edge[0]==2) {
                if (find(parents_b, edge[1]-1) == find(parents_b, edge[2]-1)) {
                    res++;
                }
                unionx(parents_b, edge[1]-1, edge[2]-1);
            }

        }
        unordered_set<int> s_a;
        unordered_set<int> s_b;
        for (int i=0; i<n; i++) {
            s_a.insert(find(parents_a, i));
            s_b.insert(find(parents_b, i));
        }
        if (s_a.size() != 1 || s_b.size() != 1) {
            return -1;
        }
        return res;
    }
};


/* You can simply plug in this class any many different codes. This class is a generic implementation of union-find. */
class UnionFind {
    vector<int> component;
    int distinctComponents;
public:
    /*
     *   Initially all 'n' nodes are in different components.
     *   e.g. component[2] = 2 i.e. node 2 belong to component 2.
     */
    UnionFind(int n) {
	    distinctComponents = n;
        for (int i=0; i<=n; i++) {
            component.push_back(i);
        }
    }

    /*
     *   Returns true when two nodes 'a' and 'b' are initially in different
     *   components. Otherwise returns false.
     */
    bool unite(int a, int b) {
        if (findComponent(a) == findComponent(b)) {
            return false;
        }
        component[findComponent(a)] = b;
        distinctComponents--;
        return true;
    }

    /*
     *   Returns what component does the node 'a' belong to.
     */
    int findComponent(int a) {
        if (component[a] != a) {
            component[a] = findComponent(component[a]);
        }
        return component[a];
    }

    /*
     *   Are all nodes united into a single component?
     */
    bool united() {
        return distinctComponents == 1;
    }
};



// ----------------- Actual Solution --------------
class Solution {

public:
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        // Sort edges by their type such that all type 3 edges will be at the beginning.
        sort(edges.begin(), edges.end(), [] (vector<int> &a, vector<int> &b) { return a[0] > b[0]; });

        int edgesAdded = 0; // Stores the number of edges added to the initial empty graph.

        UnionFind bob(n), alice(n); // Track whether bob and alice can traverse the entire graph,
                                    // are there still more than one distinct components, etc.

        for (auto &edge: edges) { // For each edge -
            int type = edge[0], one = edge[1], two = edge[2];
            switch(type) {
                case 3:
                    edgesAdded += (bob.unite(one, two) | alice.unite(one, two));
                    break;
                case 2:
                    edgesAdded += bob.unite(one, two);
                    break;
                case 1:
                    edgesAdded += alice.unite(one, two);
                    break;
            }
        }

        return (bob.united() && alice.united()) ? (edges.size()-edgesAdded) : -1; // Yay, solved.
    }
};
