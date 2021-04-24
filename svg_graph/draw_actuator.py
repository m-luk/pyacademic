from svg_graph import *

Q0 = 6600   
U = 20000
a_min = -27
a_max = 85
delta = -57
l_w = 6.6
pbar = 20 * 10**6 # Pa

l_p=248.8
l_k=456.1


def __init__(self, Q0, U, a_min, a_max, delta, l_w, pbar, l_p, l_k):
    """ Draw actuator and save it into .svg file"""
    c = canvas.canvas()


    C = point(20, 20, 'C')

    Q = pPoint( 126, radians(360+delta), C)

    P1 = pPoint( 350, radians(360+a_min), C)
    P2 = pPoint( 350, radians(360+a_max), C)

    K1= pPoint(rescale(l_w), radians(360+a_min), C)
    K2= pPoint(rescale(l_w), radians(360+a_max), C)


    Line(c, C, P1, marks=True)
    Line(c, C, P2, marks=True)
    Line(c, C, K1, marks=True)
    Line(c, C, K2, marks=True)
    Line(c, C, Q, marks=True)

    P3 = pPoint( 350, radians(360+26), C)
    K3= pPoint(rescale(l_w), radians(360+26), C)


    Line(c, C, P3, marks = True)
    Line(c, C, K3, marks = True)


    earrowLine(c, C, pPoint(700, fi=0, origin=C,))


    color = BLACK
# create actuator components

    s = l_k - l_p
# assemble the acutator
    plane = canvas.canvas()

# housing
    RectMid(plane, Q, l_p-20, 30)

# shaft extension [0-1]
    ext = 0

# shaft start and end point
    pta = Q.offset(l_p - s * (1 - ext) , 0)
    ptb = pta.offset(s, 0)

# shaft creation
    Line(plane, pta, ptb, 1.5*LINE_DEF_WIDTH, color)

# disc creation
    ptd = pta.offset(-10,0)
    RectMid(plane, ptd, 10, 30, 0, 1*LINE_DEF_WIDTH, BLACK, BLACK)

# angle
    rel = Q.relative_angle(P1)

# put on main canvas with rotation
    c.insert(plane, [trafo.rotate(180+rel, Q.x, Q.y)])


    color = RED
# create actuator components

    s = l_k - l_p
# assemble the acutator
    plane = canvas.canvas()

# housing
    RectMid(plane, Q, l_p+0, 30, linecolor=color)

# shaft extension [0-1]
    ext = 1

# shaft start and end point
    pta = Q.offset(l_p - s * (1 - ext) , 0)
    ptb = pta.offset(s, 0)

# shaft creation
    Line(plane, pta, ptb, 1.5*LINE_DEF_WIDTH, color)

# disc creation
    ptd = pta.offset(-10,0)
    RectMid(plane, ptd, 10, 30, 0, 1*LINE_DEF_WIDTH, linecolor=color, fillcolor=color)

# angle
    rel = Q.relative_angle(P2)

# put on main canvas with rotation
    c.insert(plane, [trafo.rotate(rel, Q.x, Q.y)])


    fic = abs(a_min) + abs(a_max)

    color = GREEN
# create actuator components

    s = l_k - l_p
# assemble the acutator
    plane = canvas.canvas()

# housing
    RectMid(plane, Q, l_p-0, 30, linecolor=color, mstyle=[style.linestyle.dotted])

# shaft extension [0-1]
    ext = 0.5

# shaft start and end point
    pta = Q.offset(l_p - s * (1 - ext) , 0)
    ptb = pta.offset(s, 0)

# shaft creation
    Line(plane, pta, ptb, 1.5*LINE_DEF_WIDTH, color)

# disc creation
    ptd = pta.offset(-10,0)
    RectMid(plane, ptd, 10, 30, 0, 1*LINE_DEF_WIDTH, linecolor=color, fillcolor=color)

# angle
    rel = Q.relative_angle(P3)

# put on main canvas with rotation
    c.insert(plane, [trafo.rotate(rel, Q.x, Q.y)])




    out = canvas.canvas()
    out.insert(c, [trafo.scale(0.03,0.03)])

# for pt in [P1, P2, K1, K2, Q, C]:
#     d.append(pdot(pt, 5))

    out.writeSVGfile('example')
