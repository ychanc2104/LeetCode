# https://leetcode.com/problems/design-tic-tac-toe/description/


class FileSystem:

    def __init__(self):
        self.folder = {} # split by /

    def createPath(self, path: str, value: int) -> bool:
        root = self.folder
        path_list = path.split('/')
        for i,s in enumerate(path_list):
            if s == '': continue
            if s not in root:
                if i != len(path_list)-1: # not final layer
                    return False
                root[s] = {} # final layer
            root = root[s]
        if 'value' in root:
            return False
        root['value'] = value
        return True


    def get(self, path: str) -> int:
        root = self.folder
        for s in path.split('/'):
            if s == '': continue
            if s not in root:
                return -1
            root = root[s]
        return root.get('value', -1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)