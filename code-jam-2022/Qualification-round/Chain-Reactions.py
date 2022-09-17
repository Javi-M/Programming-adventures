# N modules
# each module may point to another with lower index
# Initiators: modules that are not pointed by any others
# Initiators can be 'manually triggered'
# F_i : fun factor.

# Wile get max{F_i} fun of a chain reaction
# In total, Wile get the sum of the fun of all chain reactions

# Each module (or node) has 4 components: 
#   (index, fun_factor, it_points_to, is_triggered)
# each module points to one or none, so we don't need a list to store
# what the module is pointing at, just a number. 

T = int(input())
solutions = [] # Each solution (for each test case) is a number


for case in range(0, T):
    N = int(input()) # Number of modules of the case
    modules = [] # each module will be a dict. with 4 parameters
    initiators = []
    F = list(map(int, input().split())) # Fun factors
    P = list(map(int, input().split())) # Module i points to...(number)
    
    for i in range(0, N): # Creating modules and adding them to modules list
        m = {
            'index': i+1, 
            'fun_factor':   F[i],
            'points_to':    P[i],
            'triggered':    False
        }
        modules.append(m)
        initiators.append(m)

    for m in modules:
        p = m['points_to']
        for i in initiators:
            if i['index'] == p: # i.e, it is 'pointed'
                initiators.remove(i)

# Trying stuff:
print(modules)
print('#############')
print(len(modules))
print('#############')
print(initiators)
print('#############')
print(len(initiators))