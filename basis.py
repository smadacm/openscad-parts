import sys

from solid import *
from solid.utils import *

if 'SEGMENTS' not in globals():
    SEGMENTS = 48

def oldXRange(start, end, step):
    x = start
    while x < end:
        yield x
        x += step

def render(fn):
    results = fn()
    if type(results) != tuple:
        results = (results,)

    filename = sys.argv[0] + '.scad'

    with open(filename, 'w') as f:
        f.write('$fn = %s;'%(SEGMENTS,))
        for result in results:
            f.write('\n')
            f.write(scad_render(result))
