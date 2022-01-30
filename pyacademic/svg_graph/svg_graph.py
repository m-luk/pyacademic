from typing import get_origin
from pyx import path, canvas, style, color, deco, trafo, text
from math import radians, cos, sin, degrees, atan, acos, asin

# FIXME: aliases
rect = path.rect
circle = path.circle
line = path.line


# TODO: configs
BLACK = color.rgb.black
RED = color.rgb.red 
GREEN = color.rgb.green

POINT_RADIUS = 4
POINT_STD_COLOR = BLACK
POINT_LABEL_DEFAULT_OFFSET = (10, 10)

LINE_DEF_COLOR = BLACK
LINE_DEF_WIDTH = 2

TEXT_DEFAULT_STYLE = [text.halign.center, text.size(5), BLACK]


class point:
    def __init__(self, x, y, name=None):
        self.x = x
        self.y = y

        self.name = name

    def get_xy(self):
        return (self.x, self.y)

    def mark(self, canv, r = POINT_RADIUS, color=POINT_STD_COLOR):
        circle = path.circle(self.x, self.y, r)
        style = [color]
        
        if self.name is not None:
            canv.text(self.x+10, self.y+10, self.name, TEXT_DEFAULT_STYLE)
        canv.fill(circle, style)

    def get_delta(self, pt):
        return (pt.x-self.x, pt.y-self.y)

    def relative_angle(self, pt):
        delta = self.get_delta(pt)
        angle = round(degrees(atan(delta[1]/delta[0])), 2)
        if angle < 0:
            angle = 180 + angle
        return angle

    def offset(self, dx=0, dy=0):
        return point(self.x+dx, self.y+dy)



class pPoint (point):
    def __init__(self, r, fi = 0, origin=None, name=None):
        
        self.r = r
        self.fi = fi
        self.name = name

        if origin is not None:
            self.x = origin.x + r * cos(fi)
            self.y = origin.y + r * sin(fi)

        else:
            self.x = r * cos(fi)
            self.y = r * sin(fi)
            
     


# class Line:
#     def __init__(self, pta, ptb, linewidth = LINE_DEF_WIDTH, 
#                     color =LINE_DEF_COLOR):
#         self.line = path.line(
#             pta.x,
#             pta.y,
#             ptb.x,
#             ptb.y
#         )
#         self.color = color
#         self.linewidth = style.linewidth(linewidth)



#     def get(self):
#         return (self.line, [self.color, self.style.linewidth])


#     def show(self, canv):
#         canv.stroke()



def Line(canv, pta, ptb, linewidth = LINE_DEF_WIDTH, color=LINE_DEF_COLOR, 
            marks=False):
    line = path.line(pta.x, pta.y, ptb.x, ptb.y)

    canv.stroke(line, [style.linewidth(linewidth), color])

    if marks:
        pta.mark(canv)
        ptb.mark(canv)

def pLine(canv, pt, r, fi, linewidth = LINE_DEF_WIDTH, marks=False):

    pta = pt
    ptb = pPoint(r, fi, pt)

    line = path.line(pta.x, pta.y, ptb.x, ptb.y)

    canv.stroke(line, [style.linewidth(linewidth)])

    if marks:
        pta.mark(canv)
        ptb.mark(canv)
    

def earrowLine(canv, pta, ptb, 
                linewidth=LINE_DEF_WIDTH, 
                color=LINE_DEF_COLOR, 
                marks=False):

    line = path.line(pta.x, pta.y, ptb.x, ptb.y)

    arrow_type=deco.earrow([deco.stroked([color])], size=10)

    canv.stroke(line, [style.linewidth(linewidth), color, arrow_type])
    if marks:
        pta.mark(canv)
    


def RectMid(canv, pt, w, h, fi=0, linewidth=LINE_DEF_WIDTH, 
                linecolor=LINE_DEF_COLOR, fillcolor = None, mstyle = []):

    rect = path.rect(pt.x, pt.y - h/2, w, h)

    rto = trafo.rotate(fi, pt.x, pt.y)

    if fillcolor is not None:
        canv.fill(rect, [fillcolor, rto])

    canv.stroke(rect, [style.linewidth(linewidth), linecolor, rto] + mstyle)




def rescale(dim):
    return round(dim*100, 0)



class actuator:

    def __init__(self, origin, l_p, l_k):

        self.origin = origin
        self.lp = l_p
        self.lk = l_k

        self.s = l_k - l_p
        self.ext = 0

        self.endpoint = origin.offset(l_p, 0)

    def set_origin(self, origin):
        self.origin = origin

