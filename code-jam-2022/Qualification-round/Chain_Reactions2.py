T = int(input())
solutions = []

# Each tree node will store: fun, order, 
# each module is a node of the tree
class TreeNode:
    def _init_(self, fun, parent, index):
        self.fun = fun
        self.children = []
        self.parent = parent
        self.order = -1
        self.index = index
        self.accum_fun = fun # for the algorithm
        self.triggered = False




######## MAIN ALGORITHM


def solve_case(trees, nodes, leafs):
    # trees = [root0, root1, ...]
    # with 'tree' we refer actually to the first node, wh ich is enough
    # Note: if len(node.children)== 0, it is a leaf.
    # assign_order_children
    # node-accum_fun = max{node-fun, children-accum_fun}
    # base case: nodes which children are leafs

    # 1) accum_fun of the parents of the leafs,
    # and order of leafs
    # set: current_nodes
    # # first to the set: parents of leafs
    # if not in set: add
    
     
            
    return 0
########

for case in range(0, T):
    trees = [] # each node pointing to abyss is a tree (its root)
    nodes = [] # a list with the nodes
    leafs = []

    N = int(input()) # Number of modules of the case
    F = list(map(int, input().split())) # Fun factors
    P = list(map(int, input().split())) # Module i points to...(number)

    for i in range(0, N): # Creating nodes and adding them to modules list
        node = TreeNode(F[i], P[i], i+1)
        nodes.append(node)
        if P[i] == 0:
            trees.append(node)
    
    for i in range(0, len(nodes)):
        # if a node points to someone, it is its child:
        if P[i] != 0:
            p = P[i]
            nodes[p-1].children.append(nodes[i])

        # if no children: is a leaf
        if len(nodes[i].children) == 0:
            leafs.append(nodes[i])

    # AT THIS POINT, WE SHOULD HAVE ALL DATA STRUCTURES READY TO PLAY!



###### THE NEW IDEA
# For each test case:
## Read the input and make a tree