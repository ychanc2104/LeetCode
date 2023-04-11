// https://leetcode.com/problems/valid-parentheses/description/

// stack, TC:O(N), SC:O(N)
class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        unordered_map<char, char> memo;
        memo = {{'(', ')'}, {'[', ']'}, {'{', '}'}};
        for (char c : s) {
            // printf("%c %c %d %d %d", c, top, c==')', top=='(', stack.empty());
            if (c=='(' || c=='[' || c== '{')
                stack.push(c);
            else if (!stack.empty() && c == memo[stack.top()])
                stack.pop();
            else
                return false;
        }

        return stack.empty();
    }
};