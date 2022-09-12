T = int(input())
inputdata = []
for i in range(0, T):
    inputdata.append(input().split(' '))

def draw_punched_card(R, C):
    r = R*2 + 1 # number of rows of the real matrix of characters
    c = C*2 + 1 # num. of columns of the real matrix of characters
    for i in range(0, r):
        line = ''
        for j in range(0, c):
            if i < 2 and j < 2:
                line = line + '.'
            elif i%2 == 0:
                if j%2 == 0:
                    line = line + '+'
                else:
                    line = line + '-'
            else:
                if j%2 == 0:
                    line = line + '|'
                else:
                    line = line + '.'
        print(line) 

# The draw_punched_card function could be, likely, more elegant

for case in range(0, T):
    R = int( inputdata[case][0] )
    C = int( inputdata[case][1] ) 
    print('Case #' + str(case+1) + ':')
    draw_punched_card(R, C)