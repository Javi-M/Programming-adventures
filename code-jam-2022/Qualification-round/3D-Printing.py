T = int(input())

# a list containing triplets of printers:
triplets = []
# each triplet correspond to a test case

t = 0 # number of printers in the current triplet
newtriplet = []
for p in range(0, T*3):
    l = input().split(' ')
    printer = [] # each printer is a list of 4 numbers

    for n in l:
        printer.append(int(n))

    newtriplet.append(printer)
    t = t + 1
    
    if t == 3: # if the triplet is completed
        triplets.append(newtriplet)
        newtriplet = []
        t = 0

###########################################
# we have acces to data with this form:
# triplets[triplet][printer][color]




def casesolution(case):
    # remember: case is a triplet of printers
    # Because of restrictions of the problem:
    mins = [10**6, 10**6, 10**6, 10**6]
    for printer in case:
        for i in range(0, 3):
            if printer[i] < mins[i]:
                mins[i] = printer[i]
    
    if sum(mins) < 10**6:
        return 'IMPOSSIBLE'

    # Now that it is not impossible, we have to make the total sum: 10**6
    solution = [0, 0, 0, 0]
    total = sum(solution)
    i = 0

    while total < 10**6:
        solution[i] = mins[i]
        total = total + mins[i]
        i = i + 1
    i = i-1

    if total > 10**6:
        solution[i] = solution[i] - (total%(10**6))
        total = sum(solution)
    
    # A not elegant at all solution...
    return  str(solution[0]) + ' ' + \
            str(solution[1]) + ' ' + \
            str(solution[2]) + ' ' + \
            str(solution[3])

for case in range(0, T):
    print("Case #" + str(case+1) + ': ' + casesolution(triplets[case]))