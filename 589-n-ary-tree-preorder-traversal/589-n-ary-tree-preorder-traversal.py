# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

        
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        answer = []
        visit = [root]
        while visit:
            node = visit.pop()
            if node:
                answer.append(node.val)
                visit += [child for child in reversed(node.children)]
        return answer