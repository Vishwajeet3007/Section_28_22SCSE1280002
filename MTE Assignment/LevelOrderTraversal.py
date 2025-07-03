from collections import deque
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        ans = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            curr_level = []

            for _ in range(level_size):
                currNode = queue.popleft()
                curr_level.append(currNode.val)

                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            ans.append(curr_level)
        return ans