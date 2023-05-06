import bpy
from trickshots import *
from testbench import test

def scenario_3d():
    set_vel('ball', var3(-10, 10))
    yield hit('ball', 'box1')
    yield hit('ball', 'box2')
    yield hit('ball', 'box3')

def scenario_6d():
    set_pos('ball', var3([0, -10, 5], 5))
    set_vel('ball', var3(-10, 10))
    yield hit('ball', 'box1')
    yield hit('ball', 'box2')
    yield hit('ball', 'box3')

def escape():
    x, y, z = get_pos('ball')
    return not ((-10 < x < 10) and (-15 < y < 15) and (-5 < z < 20))

test(scenario_3d, escape)
test(scenario_6d, escape)
