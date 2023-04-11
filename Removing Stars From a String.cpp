// https://leetcode.com/problems/removing-stars-from-a-string/description/


// use stack, TC:O(N), SC:O(N)
class Solution {
public:
    string removeStars(string s) {
        string res;
        for (char c : s) {
            // char c = s[i];
            if (c == '*')
                res.pop_back();
            else
                res.push_back(c);
        }
        return res;
    }
};
