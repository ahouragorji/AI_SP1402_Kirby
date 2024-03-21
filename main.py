import numpy as np
from interface import Interface

with open('matriz.txt', 'r') as f:
    board_txt = ''.join(f.readlines()).replace('\n', ';')
world = np.matrix(board_txt)
print(world)

interface = Interface(world)
interface.showInterface()
