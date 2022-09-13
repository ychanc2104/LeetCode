# https://leetcode.com/problems/design-in-memory-file-system/
# https://leetcode.com/problems/design-in-memory-file-system/discuss/103359/Python-Straightforward-with-Explanation
# https://leetcode.com/problems/design-in-memory-file-system/discuss/426854/python-scalable-trie-solution

import collections



# separate folder and file
class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)


class FileSystem:
    def __init__(self):
        self.root = Node()
        self.content = collections.defaultdict(str)

    # TC:O(n + klogk), n is depth of input path and k is files or folders in path
    def ls(self, path: str) -> List[str]:
        # if is a file => return file's name
        # if is a directory => return all file and directory
        # print(self.paths)
        if path in self.content:
            return [path.split('/')[-1]]
        root = self.root
        for sub in path.split('/'):
            if not sub: continue
            root = root.children[sub]
        return sorted(root.children.keys())
    # TC:O(n)
    def mkdir(self, path: str) -> None:
        root = self.root
        for sub in path.split('/'):
            if not sub: continue
            root = root.children[sub]
    # TC:O(n)
    def addContentToFile(self, filePath: str, content: str) -> None:
        self.mkdir(filePath)
        self.content[filePath] += content
    # TC:O(1)
    def readContentFromFile(self, filePath: str) -> str:
        return self.content[filePath]



# merge file and folder, use content to check path is a file or a folder
class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.content = ''

class FileSystem:

    def __init__(self):
        self.root = Node()
    # find the node, TC:O(n)
    def find(self, path):
        root = self.root
        for sub in path.split('/'):
            if not sub: continue
            root = root.children[sub]
        return root
    # TC:O(n + klogk), n is depth of input path and k is files or folders in path
    def ls(self, path: str) -> List[str]:
        # if is a file => return file's name
        # if is a directory => return all file and directory
        root = self.find(path)
        if root.content:
            return [path.split('/')[-1]]
        return sorted(root.children.keys())
    # TC:O(n)
    def mkdir(self, path: str) -> None:
        self.find(path)
    # TC:O(n)
    def addContentToFile(self, filePath: str, content: str) -> None:
        root = self.find(filePath)
        root.content += content
    # TC:O(n)
    def readContentFromFile(self, filePath: str) -> str:
        root = self.find(filePath)
        return root.content

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)