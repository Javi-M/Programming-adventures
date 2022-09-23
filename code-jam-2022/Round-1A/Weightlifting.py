# W types of weights
# We have a stack: we can put weights and remove from the top
# l = [x1, x2, ..., xn] the top of the stack is xn
# l.append(value) 
# l.pop()

T = int(input())

total_solution = []

for case in range(T):
    E, W = list(map(int, input().split())) # We suppose correct input
    
    # now it comes E lines
    # each line is an exercises, with the weights required
    exercises = []
    machine_stack = []
    for i in range(E):
        pass


for case in range(T):
    print('Case #' + str(case+1) + total_solution[case])