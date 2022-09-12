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

print(triplets)