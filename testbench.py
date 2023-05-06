from trickshots import solve, set_verbosity

set_verbosity(0)

def test(scenario, *args, **kwargs):
    res = solve(scenario, *args, **kwargs)
    if res.y.finished:
        print(f'SUCCESS, {res.retries} retries, {res.iters} iters')
    else:
        print(f'FAILED, {res.retries} retries, {res.iters} iters')
