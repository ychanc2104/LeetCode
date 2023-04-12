// https://leetcode.com/problems/simplify-path/description/
// https://leetcode.com/problems/simplify-path/solutions/1847357/c-easy-stack-simple-explained-algorithm/


// stack, TC:O(N), SC:O(N)
class Solution {
public:
    string simplifyPath(string path) {
        vector<string> stack;
        for (int i=0; i<path.size(); i++) {
            if (path[i] == '/') continue;
            string temp;
            while (i < path.size() && path[i] != '/') {
                temp.push_back(path[i++]); // add single char
            }
            if (temp == ".") continue;
            if (temp == "..") {
                if (!stack.empty()) stack.pop_back();
            }
            else stack.push_back(temp);

        }

        string res = "";
        for (int i=0; i<stack.size(); i++) {
            res += "/" + stack[i];
            // res = res.append("/");
            // res = res.append(stack[i]);
        }
        return res.empty() ? "/" : res;

    }
};