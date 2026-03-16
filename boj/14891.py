from collections import deque


class Gears:
    def __init__(self):
        self.gears = []

    def add_gear(self, poles):
        gear = deque(maxlen=8)
        for pole in poles:
            gear.append(pole)
        self.gears.append(gear)

    def rotate(self, gear: int, cw: bool, to_right=None):
        # Rotate
        if (to_right is None or to_right) and (gear < 3) and (self.gears[gear][2] != self.gears[gear+1][6]):
            self.rotate(gear+1, not cw, True) # Rotate toward right
        if (to_right is None or not to_right) and (gear > 0) and (self.gears[gear][6] != self.gears[gear-1][2]):
            self.rotate(gear-1, not cw, False) # Rotate toward left
        # Shift
        if cw:
            self.gears[gear].appendleft(self.gears[gear].pop()) # Shift right
        else:
            self.gears[gear].append(self.gears[gear].popleft()) # Shift left

    def get_score(self):
        score = 0
        for idx, gear in enumerate(self.gears):
            if gear[0] == '1':
                score += pow(2, idx)
        return score
        

def main():
    gears = Gears()
    # Input
    for _ in range(4):
        gears.add_gear(input())

    K = int(input())
    for _ in range(K):
        g, count = map(int, input().split())
        g -= 1

        cw = (count > 0) # Clockwise
        for _ in range(abs(count)):
            gears.rotate(g, cw)

    print(gears.get_score())


if __name__ == "__main__":
    main()