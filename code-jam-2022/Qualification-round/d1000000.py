# Third problem from the qualifiaciton round

# A d1000000 is a dice with 1000000 sides.
# Collection of N dice.

# Input:
# T - test cases
# for each test case, two lines:
# N - number of dice
# Integers - (representing, each one, the nº of sides of its dice)

# Output: the maximum number of input dice that can be put in a straight
# (check the conditions from the original statement)

T = int(input())
total_solution = [] # This will be the list of solutions (each one a list)


def solve_case(dices):
    maxlen = 1 # We know at least a dice is received
    dices.sort()
    

    return maxlen

for case in range(0, T):
    N = input()
    line = input().split()
    dices = [int(n) for n in line] # List comprehension!
    total_solution.append(solve_case(dices))

for case in range(0, T):
    print('Case #' + str(case+1) + ':' + total_solution[case])
   