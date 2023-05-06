import bpy
import numpy as np
from trickshots import *
from testbench import test

def scenario_1d():
    a = var(6.3)
    v = 30
    set_vel('ball1', [v*np.cos(a), v*np.sin(a), 0])
    yield hit('ball1', 'ball2')
    yield hit('ball2', 'target')

def scenario_3d():
    set_vel('ball1', var3(-30, 30))
    yield hit('ball1', 'ball2')
    yield hit('ball2', 'target')

def scenario_6d():
    set_pos('ball1', var3([-9, -9, 1], [-7, -7, 1]))
    set_vel('ball1', var3(-30, 30))
    yield hit('ball1', 'ball2')
    yield hit('ball2', 'target')

def escape():
    x, y, z = get_pos('ball1')
    test = not ((-15 < x < 15) and (-12 < y < 12) and (-2 < z < 20))
    if test: return True
    x, y, z = get_pos('ball2')
    return not ((-15 < x < 15) and (-12 < y < 12) and (-2 < z < 20))

test(scenario_1d, escape)
test(scenario_3d, escape)
test(scenario_6d, escape)
