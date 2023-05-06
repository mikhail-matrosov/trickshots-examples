import bpy
from trickshots import *
from testbench import test

def scenario():
    bottle = bpy.context.scene.objects['bottle']
    set_avel(bottle, [0, -5, 0])
    set_vel(bottle, var3([0,0,0], [10, 0, 10]))
    yield hit(bottle, 'target')  # 'ground'
    yield minimize(bottle.matrix_world.to_quaternion().angle) & delay(10)
    yield minimize(bottle.matrix_world.to_quaternion().angle) & hit(bottle, 'trigger')
    yield minimize(bottle.matrix_world.to_quaternion().angle) & (wait_deactivation(bottle) | delay(100))
    yield hit(bottle, 'trigger')

def escape():
    x, y, z = get_pos('bottle')
    return not ((-5 < x < 5) and (-5 < y < 5) and (0.5 < z < 10))

test(scenario, escape)
