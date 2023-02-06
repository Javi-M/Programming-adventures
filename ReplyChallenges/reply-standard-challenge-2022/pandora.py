
# No more than one demon per turn
# Only can face demon with enough stamina
# Stamina in [0, Smax]
class Pandora:
    def __init__(self) -> None:
        pass


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

if __name__ == "__main__":
    path = "./ReplyChallenges/reply-standard-challenge-2022/00-example.txt"
    file = open(path, 'r')
    # S_i: amount stamina initial
    # S_max: max. stamina that can be accumulated
    # T: number of turns available
    # D: number of demons available
    S_i, S_max, T, D = map(lambda x: int(x), file.readline().split())

    # Getting descriptions of demons
    demons = []
    for d in range(D):
        demon_line = file.readline().split()
        
        S_c = demon_line[0]
        T_r = demon_line[1]
        S_r = demon_line[2]
        N_a = demon_line[3]
        fragments = demon_line[4:]
        demon = Demon(S_c, T_r, S_r, N_a, fragments)
        demons.append(demon)

    print(S_i, S_max, T, D)
    print(len(fragments))
    print(N_a)
    print(demons[0])