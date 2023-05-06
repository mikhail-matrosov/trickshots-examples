import bpy
import numpy as np
from trickshots import *
from testbench import test


def scenario_trig_1d():
    a = var(1.57)
    v = 15
    set_vel('ball', [0, v*np.cos(a), v*np.sin(a)])
    yield hit('ball', 'box1')
    yield hit('ball', 'trig')
    yield hit('ball', 'box3')

def scenario_trig_3d():
    set_vel('ball', var3(-20, 20))
    yield hit('ball', 'box1')
    yield hit('ball', 'trig')
    yield hit('ball', 'box3')

def scenario_trig_6d():
    set_pos('ball', var3([0, -8, 0], 1))
    set_vel('ball', var3(-20, 20))
    yield hit('ball', 'box1')
    yield hit('ball', 'trig')
    yield hit('ball', 'box3')


def scenario_1d():
    a = var(1.57)
    v = 15
    set_vel('ball', [0, v*np.cos(a), v*np.sin(a)])
    yield hit('ball', 'box1')
    yield hit('ball', 'box3')

def scenario_3d():
    set_vel('ball', var3(-20, 20))
    yield hit('ball', 'box1')
    yield hit('ball', 'box3')

def scenario_6d():
    set_pos('ball', var3([0, -8, 0], 1))
    set_vel('ball', var3(-20, 20))
    yield hit('ball', 'box1')
    yield hit('ball', 'box3')


def escape():
    x, y, z = get_pos('ball')
    return not ((-5 < x < 5) and (-10 < y < 10) and (-2 < z < 20))


for s in [scenario_trig_1d, scenario_trig_3d, scenario_trig_6d,
          scenario_1d, scenario_3d, scenario_6d]:
    test(s, escape, iters=200, retries=50)
