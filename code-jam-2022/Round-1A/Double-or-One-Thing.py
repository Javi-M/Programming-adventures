
# S1 -> min{S: S produced by S1 using "double or nothing"}
# min in lexicografical order
T = int(input())
total_solution = []

def dob(str, i): # returns string with str[i] character doubled
    return str[0:i] + str[i] + str[i:]

for case in range(0, T):
    solution = input()

    # newstr: we double the letter in the position i, solution[i]
    i = 0
    N = len(solution)
    while(i < N):
        solution = min(solution, dob(solution, i))
        if(len(solution) > N): # if size increased of the string
            i = i + (len(solution) - N)
            N = len(solution)  # with the difference above we make sure of exiting the loop
                               # still, just a fast method to implement, not a good practice
        i = i + 1

    total_solution.append(solution)

for case in range(0, T):
    print('Case #' + str(case+1) + ': ' + total_solution[case])



