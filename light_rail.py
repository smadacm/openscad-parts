import sys

from solid import *
from solid.utils import *

SEGMENTS = 48

legHeight = 8
legWidth = 1.5
legThickness = 1/8

channelHeight = 1.5
channelWidth = 1.5
channelLength = 120 # 10 feet
channelThickness = 1/8

lightSpacing = 4
lightMargin = lightSpacing / 2
lightRadius = 0.25

def lightRange(start, end, step):
    x = start
    while x < end:
        yield x
        x += step

if __name__ == '__main__':
    rail = translate([channelLength / 2 * -1, channelHeight / 2 * -1, channelWidth / 2])(
        rotate([0,90,0])(
            linear_extrude(channelLength)(
                union()(
                    square([channelHeight, channelThickness]),
                    square([channelThickness, channelWidth]),
                    translate([0, channelWidth, 0])(
                        square([channelHeight, channelThickness])
                    )
                )
            )
        )
    )

    toRemove = []
    for x in lightRange((channelLength - lightMargin) / 2 * -1, (channelLength - lightMargin) / 2, lightSpacing):
        cyl = translate([x, 0, 0])(
            cylinder(r=lightRadius, h=channelHeight, center=True)
        )
        toRemove.append(cyl)
    rail = difference()(rail, *toRemove)


    filename = sys.argv[0] + '.scad'

    with open(filename, 'w') as f:
        f.write('$fn = %s;'%(SEGMENTS,))
        f.write('\n')
        f.write(scad_render(rail))