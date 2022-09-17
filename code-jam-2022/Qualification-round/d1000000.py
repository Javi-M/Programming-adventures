# Third problem from the qualifiaciton round
# A d1000000 is a dice with 1000000 sides.

T = int(input())
total_solution = [] # This will be the list of solutions (each one a list)

# Main algorithm:
def solve_case(N:int, dices:list):
    ml = 0 # max. len. found
    dices.sort()
    for i in range(0, N):
        if dices[i] > ml:
            ml = ml + 1
    return ml

# Solving all the cases:
for case in range(0, T):
    N = int(input())
    line = input().split()
    dices = [int(n) for n in line] # List comprehension!
    total_solution.append(solve_case(N, dices))

# Printing all the cases:
total_solution = [str(c) for c in total_solution] # converting int to str
for case in range(0, T):
    print('Case #' + str(case+1) + ': ' + total_solution[case])
   