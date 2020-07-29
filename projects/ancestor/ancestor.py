
# # Note: This Queue class is sub-optimal. Why?
# class Queue():
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, value):
#         self.queue.append(value)
#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None
#     def size(self):
#         return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


# class Node:
#     def __init__(self, data, left, right):
#         self.data = data
#         self.left = left
#         self.right = right


def earliest_ancestor(self, ancestors, starting_node):
    s = Stack()
    s.push( [starting_node])
    visited = set()

    while s.size>0:
        path = s.pop()
        node = path[-1]

        if node not in visited:
            visited.add(node)
        
        if node == ancestors:
            return path
        # print(path)
        
        



#---------------------------------------------------------------
# # Data structure to store a Binary Tree node
# class Node:
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right


# # Recursive function to print all ancestors of given node in a binary tree. The
# # function returns true if node is found in subtree rooted at given root node
# def earliest_ancestor(ancestors, starting_node):

#     # base case
#     if ancestors is None:
#         return False

#     # return true if given node is found
#     if ancestors.data == starting_node:
#         return True

#     # search node in left subtree
#     left = earliest_ancestor(ancestors.left, starting_node)

#     # search node in right subtree
#     right = False
#     if not left:
#         right = earliest_ancestor(ancestors.right, starting_node)

#     # if given node is found in either left or right subtree,
#     # current node is an ancestor of given node
#     if left or right:
#         print(ancestors.data, end=' ')

#     # return true if node is found
#     return left or right


# if __name__ == '__main__':

#     # """ Construct below tree
#     #           1
#     #         /   \
#     #        /     \
#     #       2          3
#     #        \     / \
#     #         4   5   6
#     #            / \
#     #           7   8
#     # """

    # # root= Node(1)
    # # root.left = Node(2)
    # # root.right = Node(3)
    # # root.left.right = Node(4)
    # # root.right.left = Node(5)
    # # root.right.right = Node(6)
    # # root.right.left.left = Node(7)
    # # root.right.right.right = Node(8)

    # node = 1
    # earliest_ancestor(starting_node, node)




