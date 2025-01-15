class Node(object):
    def __init__(self,val,left = None, right=None):
        self.value = val
        self.left = left
        self.right = right

def BinaryTree(list_name):
    if not list_name or list_name[0] is None:
        return None
    
    root = Node(list_name[0])
    queue = [root]
    index = 1

    while queue and index < len(list_name):
        current = queue.pop(0)

        #Set to left branch if not none
        if list_name[index] is not None:
            current.left = Node(list_name[index])
            queue.append(current.left)
        index +=1

        #Check if there is right child and assign
        if index<len(list_name) and list_name[index] is not None:
            current.right = Node(list_name[index])
            queue.append(current.right)
        index+=1

    return root

list_name = [1,4,2,3,5,1,2]
root = BinaryTree(list_name)


########################################################### TRAVERSALS ################################################################
#BFS or Level Order
def bfs(root):
    if not root:
        return []
    
    result = []
    queue = [root]

    while queue:
        level = []
        for _ in range(len(queue)):
            node=queue.pop(0)
            if node:
                level.append(node.value)
                queue.append(node.left)
                queue.append(node.right)
        if level:
            result.append(level)
    return result

print(bfs(root))

