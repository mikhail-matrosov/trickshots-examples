import bpy
import numpy as np
from trickshots import *
from testbench import test

def scenario_1d():
    a = var(3.14)
    v = 10
    set_vel('Cube', [0, v*np.cos(a), v*np.sin(a)])
    yield hit('Cube', 'target')

def scenario_3d():
    set_vel('Cube', var3(-10, 10))
    yield hit('Cube', 'target')

def scenario_6d():
    set_pos('Cube', var3([0,-5,0], 1))
    set_vel('Cube', var3(-10, 10))
    yield hit('Cube', 'target')

def escape():
    x, y, z = get_pos('Cube')
    return not ((-5 < x < 5) and (-10 < y < 10) and (-5 < z < 10))

test(scenario_1d, escape)
test(scenario_3d, escape)
test(scenario_6d, escape)
