import bpy
from trickshots import *
from testbench import test

def scenario():
    set_vel('ball', var3([-20,-5,0], [-5,0,0]))
    yield hit('ball', 'ceil')
    yield hit('ball', 'target')

def escape():
    x, y, z = get_pos('ball')
    return not ((-1 < x < 1) and (-1 < y < 1) and (0 < z < 2))

test(scenario, escape)
