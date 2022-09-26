# W types of weights
# We have a stack: we can put weights and remove from the top
# l = [x1, x2, ..., xn] the top of the stack is xn
# l.append(value) 
# l.pop()

T = int(input())

total_solution = []

##
# EXERCISES MUST BE DONE IN ORDER
# Def. distance: n_ops(stack1, stack2)
# Representations of stacks, 2 examples:
# [1, 1, 1, 2, 2, 2]
# [1, 2, 1, 2, 1, 2]
# would mean: 3 discs type 1, 3 discs type 2.
def n_ops(s1, s2):
    n = 0
    i = 0
    while (i < len(s1) and s1[i]==s2[i]):
        i = i+1
    if i < range(len(s1)): # i.e: they are not the same stack
        n = (len(s1) - i)*2
    return n

for case in range(T):
    E, W = list(map(int, input().split())) # We suppose correct input.
    
    # Now it comes E lines.
    # Each line is an exercises, with the weights required.
    # [4, 5, 6] -> 4 weights of type 1. 6 weights of type 3. 5w type 2.

    # Exercises is a matrix. Each row contains the weights for an exercies.
    exercises = []
    weights = []
    # machine_stack = []
    for i in range(E):
        weights = list(map(int, input().split()))
        exercises.append(weights)
        pass

for r in exercises:
    print(r)

# for case in range(T):
#     print('Case #' + str(case+1) + total_solution[case])