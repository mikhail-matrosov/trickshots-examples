import bpy
from trickshots import *
from testbench import test

def scenario():
    set_vel('cube', var3(-10, 10))
    yield hit('cube', 'target1')
    set_vel('cube', var3(-10, 10))
    yield hit('cube', 'target2')

def escape():
    x, y, z = get_pos('cube')
    return not ((-12 < x < 5) and (-10 < y < 10) and (-5 < z < 10))

test(scenario, escape)
