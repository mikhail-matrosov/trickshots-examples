import bpy
from trickshots import *
from testbench import test

def scenario():
    yield delay(var(50))
    set_vel('ball', [0, var(10, 20), var(0, 10)])
    yield hit('ball', 'trig')
    yield hit('ball', 'pendulum')
    yield hit('ball', 'target')

def escape():
    x, y, z = get_pos('ball')
    return not ((-5 < x < 5) and (-11 < y < 11) and (-1 < z < 10))

test(scenario, escape)
