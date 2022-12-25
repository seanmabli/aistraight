import random
import math
import numpy as np
pi = np.pi

# board size: 236 cm by 118 cm
location = [[pi / 4, 118, 57]]
movement = []

for _ in range(3):
    while True:
        turn = random.uniform(-2 * pi, 2 * pi)
        straight = random.randint(0, 150)

        newangle = location[-1][0] + turn
        if newangle < 0: newangle += 2 * pi
        if newangle > 360: newangle = newangle % 2 * pi

        if newangle == 0:
            horizontal = straight.copy()
            vertical = 0
        elif newangle == pi / 2:
            horizontal = 0
            vertical = straight.copy()
        elif newangle == pi:
            horizontal = -straight.copy()
            vertical = 0
        elif newangle == pi * 1.5:
            horizontal = 0
            vertical = -straight.copy()
        elif 0 < newangle < pi / 2:
            horizontal = math.cos(newangle) * straight
            vertical = math.sin(newangle) * straight
        elif pi / 2 < newangle < pi:
            horizontal = - math.cos(pi - newangle) * straight
            vertical = math.sin(pi - newangle) * straight
        elif pi < newangle < pi * 1.5:
            horizontal = - math.cos(newangle - pi) * straight
            vertical =  - math.sin(newangle - pi) * straight
        elif pi * 1.5 < newangle < pi * 2:
            horizontal = math.cos(pi * 2 - newangle) * straight
            vertical = - math.sin(pi * 2 - newangle) * straight

        newhorizontal = location[-1][1] + horizontal
        newvertical = location[-1][2] + vertical

        if 0 < newhorizontal < 236 and 0 < newvertical < 118:
            location.append([newangle, newhorizontal, newvertical])
            movement.append([turn, straight])
            break