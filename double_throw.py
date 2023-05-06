import bpy
import numpy as np
from trickshots import *
from testbench import test

def scenario_2d():
    a1 = var(3.14)
    a2 = 1.6-var(3.14)
    v = 10
    set_vel('cube1', [0, v*np.cos(a1), v*np.sin(a1)])
    set_vel('cube2', [0, v*np.cos(a2), v*np.sin(a2)])
    yield hit('cube1', 'target1') & hit('cube2', 'target2')

def scenario_4d():
    set_vel('cube1', var3(-10, 10))
    set_vel('cube2', var3(-10, 11))
    yield trigger(hit('cube1', 'target1')) & trigger(hit('cube2', 'target2'))

def escape():
    x, y, z = get_pos('cube1')
    return not ((-10 < x < 10) and (-10 < y < 10) and (-5 < z < 15))
    x, y, z = get_pos('cube2')
    return not ((-10 < x < 10) and (-10 < y < 10) and (-5 < z < 15))

test(scenario_2d, escape, retries=2, iters=200)
test(scenario_4d, escape, retries=2, iters=200)
