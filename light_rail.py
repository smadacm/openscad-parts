from basis import *

legHeight = 8
legWidth = 1.5
legThickness = 1/8
legSpacing = 12
legMargin = legSpacing / 2

channelHeight = 1.5
channelWidth = 1.5
channelLength = 72 # 6 feet
channelThickness = 1/8

lightSpacing = 4
lightMargin = lightSpacing / 2
lightRadius = 0.25

def target():
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
    for x in oldXRange((channelLength - lightMargin) / 2 * -1, (channelLength - lightMargin) / 2, lightSpacing):
        cyl = translate([x, 0, 0])(
            cylinder(r=lightRadius, h=channelHeight, center=True)
        )
        toRemove.append(cyl)
    rail = difference()(rail, *toRemove)

    legs = []
    legZ = (legHeight / 2 * -1) + channelHeight / 2 - channelThickness
    legYLeft = channelWidth / 2 - channelThickness
    legYRight = legYLeft * -1
    for i,x in enumerate(oldXRange((channelLength - legMargin) / 2 * -1, (channelLength - legMargin) / 2, legSpacing)):
        leg = translate([x, legYLeft if i%2 else legYRight, legZ])(
            cube([legWidth, legThickness, legHeight], center=True)
        )
        legs.append(leg)
    rail = union()(rail, *legs)

    return rail

if __name__ == '__main__':
    render(target)
