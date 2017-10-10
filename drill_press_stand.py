import sys

from solid import *
from solid.utils import *

SEGMENTS = 48

legWidth = 1.5
legHeight = 42
legOffsetX = 5
legOffsetY = 8
legAngle = 15

"""
(1, 1) = (1, -1)
(1, -1) = (-1, -1)
(-1, 1) = (1, 1)
(-1, -1) = (-1, 1)
"""

def leg(xPos=True, yPos=True):
    xCo = 1 if xPos else -1
    yCo = 1 if yPos else -1

    angleOffsetX = cos(legAngle) * legHeight * xCo
    offsetX = legOffsetX * xCo + angleOffsetX / 2

    angleOffsetY = cos(legAngle) * legHeight * yCo
    offsetY = legOffsetY * yCo + angleOffsetY / 2

    angleX = legAngle * yCo * -1
    angleY = legAngle * xCo * 1

    print('X: ', angleOffsetX, offsetX, angleX)
    print('Y: ', angleOffsetY, offsetY, angleY)

    l = translate([offsetX, offsetY, 0])(
        rotate(a=[angleX, angleY, 0])(
            cube((legWidth, legWidth, legHeight))
        )
    )

    return l

if __name__ == '__main__':
    l1 = leg(xPos=True, yPos=True)
    l2 = leg(xPos=True, yPos=False)
    l3 = leg(xPos=False, yPos=True)
    l4 = leg(xPos=False, yPos=False)

    topZ = sin(legAngle) * legHeight
    top1 = translate((0, legOffsetY, topZ))(cube((2 * legOffsetX, legWidth, legWidth), center=True))

    filename = sys.argv[0] + '.scad'

    with open(filename, 'w') as f:
        f.write('$fn = %s;'%(SEGMENTS,))
        f.write('\n')
        f.write(scad_render(l1))
        f.write('\n')
        f.write(scad_render(l2))
        f.write('\n')
        f.write(scad_render(l3))
        f.write('\n')
        f.write(scad_render(l4))
        f.write('\n')

        f.write(scad_render(top1))
        f.write('\n')
