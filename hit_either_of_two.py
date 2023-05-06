import bpy
import numpy as np
from trickshots import *
from testbench import test

norm = np.linalg.norm


def scenario():
    set_vel('cube', var3(-15, 15))
    yield hit('cube', 'target1') | hit('cube', 'target2')

def escape():
    x, y, z = get_pos('cube')
    return not ((-15 < x < 15) and (-15 < y < 15) and (-5 < z < 20))


n1 = n2 = 0
for i in range(20):
    res = solve(scenario, escape)

    if res.y.finished:
        print(f'success, {res.retries} retries, {res.iters} iters')
    else:
        print(f'failed, {res.retries} retries, {res.iters} iters')

    if res.y.finished:
        d1 = norm(get_pos('cube') - get_pos('target1'))
        d2 = norm(get_pos('cube') - get_pos('target2'))
        if d1 < d2:
            n1 += 1
        else:
            n2 += 1
        if n1 and n2:
            print(f'SUCCESS, {n1=}, {n2=}')
            break
