
# No more than one demon per turn
# Only can face demon with enough stamina
# Stamina in [0, Smax]
class Pandora:
    def __init__(self, S_i, S_max, T) -> None:
        self.turns_left = T
        self.S_i = S_i
        self.S_max = S_max

    def __str__(self) -> str:
        return "S_i: {}\nS_max: {}\nTurns left: {}".format(self.S_i, self.S_max, self.turns_left)

class Demon:
    def __init__(self, S_c, T_r, S_r, N_a, fragments):
        self.S_c = S_c
        self.T_r = T_r
        self.S_r = S_r
        self.N_a = N_a
        self.fragments = fragments
        pass

    def __str__(self) -> str:
        return "S_c: {}\nT_r: {}\nS_r: {}\nN_a: {}\nfragments:{}"\
            .format(self.S_c, self.T_r, self.S_r, self.N_a, self.fragments)

    def reward(self, turns_left):
        """Total fragments earned after defeating"""
        return sum(self.fragments[:(turns_left-1)])
    
if __name__ == "__main__":

    # READING INITIAL CONDITIONS:
    inputfile = "00-example.txt"
    path = "./ReplyChallenges/reply-standard-challenge-2022/{}".format(inputfile)
    file = open(path, 'r')

    # S_i: amount stamina initial
    # S_max: max. stamina that can be accumulated
    # T: number of turns available
    # D: number of demons available
    S_i, S_max, T, D = map(lambda x: int(x), file.readline().split())
    turns_left = T

    # READING descriptions of demons
    demons = []
    rewards = []
    staminas_c = []
    turns_r = []
    demons_fragments = []
    confrontable = [] # True iif S_i > S_c
    for d in range(D):
        demon_line = list(map(int, file.readline().split())) # There are only integers
        S_c = demon_line[0] # Stamina to confront the demon
        T_r = demon_line[1] # Turns before recovering stamina
        S_r = demon_line[2] # Stamina recovered
        N_a = demon_line[3] # Fragments earned
        fragments = demon_line[4:]
        demon = Demon(S_c, T_r, S_r, N_a, fragments)
        demons.append(demon)
        
        staminas_c.append(S_c)
        confrontable.append(S_i > S_c)           # must be actualize each turn
        rewards.append(demon.reward(turns_left)) # must be actualize each turn
    
    E = [] # Demons to fight, in order. SOLUTION HERE
    ###### BIG BRAIN THINKING HERE (main algorithm) ######
    # Try to confront higher reward
    paths = [] # each path is an order of fighting the demons
    paths_current_rewards = [] # the current reward of each path explored

    i = rewards.index(max(rewards))
    print(confrontable)
    print(staminas_c[i])
    if S_i > staminas_c[i]:
        print(staminas_c[i])

    ###### BIG BRAIN THINKING ENDS ######

    # PRINTING THE SOLUTION: OUTPUT-<scenario name>.txt
    scenario = ""
    path = "./ReplyChallenges/reply-standard-challenge-2022/output-{}.txt".format(scenario)
    output = open(path, "w")
    for d in E:
        output.write(str(d)+"\n")