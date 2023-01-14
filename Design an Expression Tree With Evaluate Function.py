# https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/description/
# https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/solutions/910018/c-python-the-intended-solution-during-the-interview-polymorphism/
# https://stackoverflow.com/questions/12516/expression-evaluation-and-tree-walking-using-polymorphism-ala-steve-yegge#%20define%20your%20fields%20here%20%20%20%20def%20evaluate(self)%20-%3E%20int:%20%20%20%20%20%20%20%20passclass%20BinaryNode(Node):%20%20%20%20%22%22%22base%20class%20for%20binary%20nodes%22%22%22%20%20%20%20def%20__init__(self,%20_left,%20_right):%20%20%20%20%20%20%20%20self.left%20=%20_left%20%20%20%20%20%20%20%20self.right%20=%20_right%20%20%20%20def%20evaluate(self)%20-%3E%20int:%20%20%20%20%20%20%20%20passclass%20Plus(BinaryNode):%20%20%20%20def%20evaluate(self)%20-%3E%20int:%20%20%20%20%20%20%20%20return%20self.left.evaluate()%20+%20self.right.evaluate()class%20Minus(BinaryNode):%20%20%20%20def%20evaluate(self)%20-%3E%20int:%20%20%20%20%20%20%20%20return%20self.left.evaluate()%20-%20self.right.evaluate()class%20Mul(BinaryNode):%20%20%20%20def%20evaluate(self)%20-%3E%20int:%20%20%20%20%20%20%20%20return%20self.left.evaluate()%20*%20self.right.evaluate()class%20Div(BinaryNode):%20%20%20%20def%20evaluate(self)%20-%3E%20int:%20%20%20%20%20%20%20%20return%20self.left.evaluate()%20//%20self.right.evaluate()class%20Num(Node):%20%20%20%20def%20__init__(self,%20_value):%20%20%20%20%20%20%20%20self.value%20=%20_value%20%20%20%20def%20evaluate(self)%20-%3E%20int:%20%20%20%20%20%20%20%20return%20self.value%22%22%22%20%20%20%20This%20is%20the%20TreeBuilder%20class.You%20can%20treat%20it%20as%20the%20driver%20code%20that%20takes%20the%20postinfix%20inputand%20returns%20the%20expression%20tree%20represnting%20it%20as%20a%20Node.%22%22%22class%20TreeBuilder(object):%20%20%20%20def%20buildTree(self,%20postfix:%20List[str])%20-%3E%20'Node':%20%20%20%20%20%20%20%20operators%20=%20{'+':%20Plus,%20'-':%20Minus,%20'*':%20Mul,%20'/':%20Div}%20%20%20%20%20%20%20%20stk%20=%20[]%20%20%20%20%20%20%20%20for%20token%20in%20postfix:%20%20%20%20%20%20%20%20%20%20%20%20if%20token%20in%20operators:%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20R%20=%20stk.pop()%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20L%20=%20stk.pop()%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20stk.append(operators[token](L,%20R))%20%20%20%20%20%20%20%20%20%20%20%20else:%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20stk.append(Num(int(token)))%20%20%20%20%20%20%20%20return%20stk[0]%22%22%22Your%20TreeBuilder%20object%20will%20be%20instantiated%20and%20called%20as%20such:obj%20=%20TreeBuilder();expTree%20=%20obj.buildTree(postfix);ans%20=%20expTree.evaluate();%22%22%22%20%20%20%20%20%20%20135135Previous[c++]%20[0ms]%20[100%]%20a%20few%20tricks%20for%20better%20performaceNextEasy%20to%20understand%20python%20solution%20(uses%20eval)Comments%20(14)yinghanma97Jun%2006,%202021java%20version:/**%20*%20This%20is%20the%20interface%20for%20the%20expression%20tree%20Node.%20*%20You%20should%20not%20remove%20it,%20and%20you%20can%20define%20some%20classes%20to%20implement%20it.%20*/abstract%20class%20Node%20{%20%20%20%20public%20abstract%20int%20evaluate();%20%20%20%20//%20define%20your%20fields%20here};class%20NumNode%20extends%20Node%20{%20%20%20%20int%20val;%20%20%20%20public%20NumNode(int%20val)%20{%20%20%20%20%20%20%20%20this.val%20=%20val;%20%20%20%20}%20%20%20%20%20%20%20%20public%20int%20evaluate()%20{%20%20%20%20%20%20%20%20return%20val;%20%20%20%20}}abstract%20class%20OpNode%20extends%20Node%20{%20%20%20%20Node%20left;%20%20%20%20Node%20right;%20%20%20%20%20%20%20%20public%20OpNode(Node%20left,%20Node%20right)%20{%20%20%20%20%20%20%20%20this.left%20=%20left;%20%20%20%20%20%20%20%20this.right%20=%20right;%20%20%20%20}}class%20AddOpNode%20extends%20OpNode%20{%20%20%20%20public%20AddOpNode(Node%20left,%20Node%20right)%20{%20%20%20%20%20%20%20%20super(left,%20right);%20%20%20%20}%20%20%20%20public%20int%20evaluate()%20{%20%20%20%20%20%20%20%20return%20this.left.evaluate()%20+%20this.right.evaluate();%20%20%20%20}}class%20SubOpNode%20extends%20OpNode%20{%20%20%20%20public%20SubOpNode(Node%20left,%20Node%20right)%20{%20%20%20%20%20%20%20%20super(left,%20right);%20%20%20%20}%20%20%20%20public%20int%20evaluate()%20{%20%20%20%20%20%20%20%20return%20this.left.evaluate()%20-%20this.right.evaluate();%20%20%20%20}}class%20MultiplyOpNode%20extends%20OpNode%20{%20%20%20%20%20public%20MultiplyOpNode(Node%20left,%20Node%20right)%20{%20%20%20%20%20%20%20%20super(left,%20right);%20%20%20%20}%20%20%20%20%20%20%20%20public%20int%20evaluate()%20{%20%20%20%20%20%20%20%20return%20this.left.evaluate()%20*%20this.right.evaluate();%20%20%20%20}}class%20DivideOpNode%20extends%20OpNode%20{%20%20%20%20%20public%20DivideOpNode(Node%20left,%20Node%20right)%20{%20%20%20%20%20%20%20%20super(left,%20right);%20%20%20%20}%20%20%20%20public%20int%20evaluate()%20{%20%20%20%20%20%20%20%20return%20this.left.evaluate()%20/%20this.right.evaluate();%20%20%20%20}}/**%20*%20This%20is%20the%20TreeBuilder%20class.%20*%20You%20can%20treat%20it%20as%20the%20driver%20code%20that%20takes%20the%20postinfix%20input%20%20*%20and%20returns%20the%20expression%20tree%20represnting%20it%20as%20a%20Node.%20*/class%20TreeBuilder%20{%20%20%20%20Node%20buildTree(String[]%20postfix)%20{%20%20%20%20%20%20%20%20Stack%3CNode%3E%20st%20=%20new%20Stack%3C%3E();%20%20%20%20%20%20%20%20for(String%20token%20:%20postfix)%20{%20%20%20%20%20%20%20%20%20%20%20%20if%20(Character.isDigit(token.charAt(0)))%20{%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20st.push(new%20NumNode(Integer.parseInt(token)));%20%20%20%20%20%20%20%20%20%20%20%20}%20else%20{%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20Node%20right%20=%20st.pop();%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20Node%20left%20=%20st.pop();%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20st.push(buildNode(token,%20left,%20right));%20%20%20%20%20%20%20%20%20%20%20%20}%20%20%20%20%20%20%20%20}%20%20%20%20%20%20%20%20return%20st.peek();%20%20%20%20}%20%20%20%20%20%20%20%20private%20Node%20buildNode(String%20op,%20Node%20left,%20Node%20right)%20{%20%20%20%20%20%20%20%20switch(op)%20{%20%20%20%20%20%20%20%20%20%20%20%20case%20%22+%22:%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20new%20AddOpNode(left,%20right);%20%20%20%20%20%20%20%20%20%20%20%20case%20%22-%22:%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20new%20SubOpNode(left,%20right);%20%20%20%20%20%20%20%20%20%20%20%20case%20%22*%22:%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20new%20MultiplyOpNode(left,%20right);%20%20%20%20%20%20%20%20%20%20%20%20case%20%22/%22:%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20new%20DivideOpNode(left,%20right);%20%20%20%20%20%20%20%20%20%20%20%20default:%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20null;%20%20%20%20%20%20%20%20}%20%20%20%20}};/**%20*%20Your%20TreeBuilder%20object%20will%20be%20instantiated%20and%20called%20as%20such:%20*%20TreeBuilder%20obj%20=%20new%20TreeBuilder();%20*%20Node%20expTree%20=%20obj.buildTree(postfix);%20*%20int%20ans%20=%20expTree.evaluate();%20*/Read%20more31Show%204%20RepliesReplyysonglcOct%2029,%202020+1I%20believe%20the%20intention%20of%20this%20problem%20is%20to%20test%20a%20candidate's%20proficiency%20in%20the%20OOD%20by%20implementing%20the%20interface.15ReplygrokusOct%2031,%202020+1%20for%20Python%20solution%20using%20polymorphism.11ReplypolasprawkaFeb%2025,%202021Isn't%20the%20whole%20idea%20of%20polymorphism%20to%20get%20rid%20of%20if/else%20or%20switch%20statements?%20%20%20%20%20%20%20%20%20%20%20%20if%20op%20==%20%22+%22:%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20Plus(left,%20right)%20%20%20%20%20%20%20%20%20%20%20%20elif%20op%20==%20%22-%22:%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20Minus(left,%20right)%20%20%20%20%20%20%20%20%20%20%20%20elif%20op%20==%20%22*%22:%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20Mul(left,%20right)%20%20%20%20%20%20%20%20%20%20%20%20elif%20op%20==%20%22/%22:%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20Div(left,%20right)8Show%201%20RepliesReplyice_cube918100%20Days%20Badge%202022Dec%2004,%202021Awesome%20solution!%20But%20I%20think%20this%20question%20should%20be%20hard.3Replyash_pdx50%20Days%20Badge%202022Oct%2012,%202021I%20don't%20understand%20the%20advantage%20of%20having%20the%20BinaryClass.%20We%20can%20define%20the%20fields%20in%20the%20Node%20class%20and%20all%20the%20other%20classes%20inherit%20from%20the%20Node%20class.1Replysid-ant50%20Days%20Badge%202022Jul%2013,%202021Thanks%20for%20this%20solution.%20Here%20the%20tree%20is%20an%20object%20of%20objects.Basically%20for%20expression:[%223%22,%224%22,%22+%22,%222%22,%22*%22,%227%22,%22/%22]You'll%20have%20this%20outputdiv%20(%20mul%20(%20plus%20(%20num(3)%20,%20num(4)%20)%20,%20num(2)%20)%20,%20num(7)%20)1Replyyinghanma97Jun%2006,%202021This%20is%20the%20best%20solution1ReplyanaloglifeJan%2001,%202021can%20someone%20please%20explain%20how%20this%20works?return%20self.left.evaluate()%20+%20self.right.evaluate()why%20not%20just?return%20self.left+self.right1Show%201%20RepliesReplyfbookzone100%20Days%20Badge%202022Jul%2027,%202022If%20you%20ignore%20polymorphism,%20you%20can%20use%20unordered_map%20to%20get%20rid%20of%20if%20elseunordered_map%3Cstring,%20function%3Cint(int,%20int)%3E%3E%20ops_%20{%20%20%20%20{%22+%22,%20[](int%20a,%20int%20b)%20{%20return%20a%20+%20b;%20}},%20%20%20%20{%22-%22,%20[](int%20a,%20int%20b)%20{%20return%20a%20-%20b;%20}},%20%20%20%20{%22*%22,%20[](int%20a,%20int%20b)%20{%20return%20a%20*%20b;%20}},%20%20%20%20{%22/%22,%20[](int%20a,%20int%20b)%20{%20return%20a%20/%20b;%20}},};0ReplyComments14Favorited0Views8.8K

import abc
from abc import ABC, abstractmethod
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class BinaryNode(Node):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

class Num(Node):
    def __init__(self, val):
        self.val = val

    def evaluate(self):
        return int(self.val)

class Add(BinaryNode):
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

class Minus(BinaryNode):
    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()

class Mul(BinaryNode):
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()

class Div(BinaryNode):
    def evaluate(self):
        return int(self.left.evaluate() / self.right.evaluate())

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        opt = {'+': Add, '-': Minus, '*': Mul, '/': Div}
        stack = []
        for s in postfix:
            if s in opt:
                node = opt[s](right=stack.pop(), left=stack.pop())
            else:
                node = Num(s)
            stack.append(node)
        return stack.pop()


class TreeBuilder2(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        opt = {'+': Add, '-': Minus, '*': Mul, '/': Div}
        def dfs():
            if postfix:
                s = postfix.pop()
                if s in opt:
                    node = opt[s]()
                    node.right = dfs()
                    node.left = dfs()
                    return node
                return Num(s)

        return dfs()

opt = {'+': Add, '-': Minus, '*': Mul, '/': Div}

class TreeBuilder3(object):

    def buildTree(self, postfix: List[str]) -> 'Node':
        # must end with +-*/ and start with num
        s = postfix.pop()
        if s in opt:
            node = opt[s]()
            node.right = self.buildTree(postfix)
            node.left = self.buildTree(postfix)
            return node
        return Num(s)


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""