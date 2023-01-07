from itertools import permutations

# To solve "indexing confusion": right shift to input lists: F and P
# Also right shift triggered
def trigger(idx, triggered, F, P):
    max_fun = F[idx]

    if triggered[idx]:
        return 0

    triggered[idx] = True

    if P[idx] == 0:
        return F[idx]
    else:
        idx2 = P[idx]
        f2 = trigger(idx2, triggered, F, P)
        max_fun = max(max_fun, f2)

    return max_fun



def solve_case(N, F, P):
    F2 = [0] + F     # RIGHT SHIFT
    P2 = [0] + P     # RIGHT SHIFT

    inis = range(1, N+1)
    initiators = [x for x in inis if not x in P2] # Not pointed by anything

    all_possible_orders = list(permutations(initiators))

    max_fun = 0

    for order in all_possible_orders:
        order_fun = 0
        triggered = [True] + [False]*N # RIGHT SHIFT
        for i in order:
            chain_fun = trigger(i, triggered, F2, P2)
            order_fun = order_fun + chain_fun
        
        if order_fun > max_fun:
            max_fun = order_fun

    return max_fun

if __name__ == "__main__":
    solutions = []

    T = int(input())

    for case in range(T):
        # Each test case has 3 input lines
        N = int(input()) # Number of modules of the case
        F = list(map(int, input().split())) # Fun factors
        P = list(map(int, input().split())) # Module i points to P[i] (number)
        solutions.append(solve_case(N, F, P))

    solutions = [str(c) for c in solutions] # converting int to str

    for case in range(T):
        print('Case #' + str(case+1) + ': ' + solutions[case])