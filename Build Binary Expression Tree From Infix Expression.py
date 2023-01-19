# https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/
# https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/solutions/949053/python3-two-stacks-approach-ops-nums-stacks/
# https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/solutions/864596/python-standard-parser-implementation/


# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def expTree(s: str) -> 'Node':
    # l=>root=>r
    def parse():
        node = opts.pop()
        node.right = nums.pop()
        node.left = nums.pop()
        nums.append(node)

    nums = []  # store number's Node
    opts = []  # to store operators (presign)
    for c in s:
        if c.isdigit():
            nums.append(Node(c))
            continue
        elif c == ')':
            while opts[-1].val != '(':  # parse to its pair
                parse()
            opts.pop()  # pop out '('
            continue
        elif c in '+-':  # directly append previous
            while opts and opts[-1].val in '+-*/':  # continuously pop two nums because of encountering +- => all operands can be done
                parse()
        elif c in '*/':  # if previous is also */ can be directly append
            if opts and opts[-1].val in '*/':  # pop two nums
                parse()
        opts.append(Node(c))

    while opts:
        parse()

    return nums[0]


import collections
class Solution2:
    # Standard parser implementation based on this BNF
    #   s := expression
    #   expression := term | term { [+,-] term] }
    #   term := factor | factor { [*,/] factor] }
    #   factor :== digit | '(' expression ')'
    #   digit := [0..9]

    def expTree(self, s: str) -> 'Node':
        tokens = collections.deque(list(s))
        return self.parse_expression(tokens)

    def parse_expression(self, tokens):
        lhs = self.parse_term(tokens)
        while len(tokens) > 0 and tokens[0] in ['+', '-']:
            op = tokens.popleft()
            rhs = self.parse_term(tokens)
            lhs = Node(val=op, left=lhs, right=rhs)
        return lhs

    def parse_term(self, tokens):
        lhs = self.parse_factor(tokens)
        while len(tokens) > 0 and tokens[0] in ['*', '/']:
            op = tokens.popleft()
            rhs = self.parse_factor(tokens)
            lhs = Node(val=op, left=lhs, right=rhs)
        return lhs

    def parse_factor(self, tokens):
        if tokens[0] == '(':
            tokens.popleft()  # consume '('
            node = self.parse_expression(tokens)
            tokens.popleft()  # consume ')'
            return node
        else:
            # Single operand
            token = tokens.popleft()
            return Node(val=token)