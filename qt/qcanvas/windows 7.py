from pyx import *
from math import *
from pyx.metapost.path import beginknot, endknot, smoothknot, tensioncurve

def Liniastart(y):
    x = -0.3

    pg1, pg2, pg3 = (0.25 + 6.5 * x, sin(0 + x)*0.3+y), (1 + 7.5 * x, sin(1 + x)*0.3+y), (2 + 7 * x, sin(2 + x)*0.3+y)
    pg4, pg5, pg6 = (3 + 8 * x, sin(3 + x)*0.3+y), (4 + 8 * x, sin(4 + x)*0.3+y), (4.5 + 8 * x, sin(15 + x)*0.03+y)
    path = metapost.path.path([
        beginknot(*pg1), tensioncurve(), smoothknot(*pg2), tensioncurve(),
        smoothknot(*pg3), tensioncurve(), smoothknot(*pg4), tensioncurve(),
        smoothknot(*pg5), tensioncurve(), endknot(*pg6)])
    return path

def Liniasrodek(y):
    x = -0.32

    pg1, pg2, pg3 = (0.2 + 6.5 * x, sin(0 + x)*0.3+y), (1 + 8 * x, sin(1 + x)*0.3+y), (2 + 7.5 * x, sin(2 + x)*0.3+y)
    pg4, pg5, pg6 = (3 + 8 * x, sin(3 + x)*0.3+y), (4 + 8 * x, sin(4 + x)*0.3+y), (4.5 + 8 * x, sin(15 + x)*0.03+y)
    path = metapost.path.path([
        beginknot(*pg1), tensioncurve(), smoothknot(*pg2), tensioncurve(),
        smoothknot(*pg3), tensioncurve(), smoothknot(*pg4), tensioncurve(),
        smoothknot(*pg5), tensioncurve(), endknot(*pg6)])
    return path


def Liniakoniec(y):
    x = -0.35

    pg1, pg2, pg3 = (0.25 + 6.5 * x, sin(0 + x)*0.3+y), (1 + 8 * x, sin(1 + x)*0.3+y), (2 + 7 * x, sin(2 + x)*0.3+y)
    pg4, pg5, pg6 = (3 + 8 * x, sin(3 + x)*0.3+y), (4 + 8 * x, sin(4 + x)*0.3+y), (4.5 + 8 * x, sin(15 + x)*0.03+y)
    path = metapost.path.path([
        beginknot(*pg1), tensioncurve(), smoothknot(*pg2), tensioncurve(),
        smoothknot(*pg3), tensioncurve(), smoothknot(*pg4), tensioncurve(),
        smoothknot(*pg5), tensioncurve(), endknot(*pg6)])
    return path

c = canvas.canvas()

kolo1 = path.circle(0, 0, 3.7)
styl1 = [style.linewidth(1.9), style.linecap.round, color.rgb.white]

czerwony = [color.rgb(237/256.0,51/256.0,0/256.0)]
zielony = [color.rgb(81/256.0,211/256.0,0/256.0)]
niebieski = [color.rgb(6/256.0,142/256.0,226/256.0)]
zolty = [color.rgb(237/256.0,213/256.0,0/256.0)]

fala_tlo = [color.rgb(23/256.0,77/256.0,165/256.0)]

c.fill(kolo1, [color.rgb(23/256.0,77/256.0,165/256.0)])

c.fill(path.rect(-1.6,0,1.9,1.6), czerwony)
c.fill(path.rect(0.1,-0.2,1.7,1.62), zielony)
c.fill(path.rect(-1.8,-1.5,1.7,1.6), niebieski) 
c.fill(path.rect(-0.1,-1.65,1.7,1.556), zolty)

c.stroke(path.line(-2,-2,-1.4,1.95),[style.linewidth(0.3), color.rgb(23/256.0,77/256.0,165/256.0)])
c.stroke(path.line(-0.3,-2,0.3,2),[style.linewidth(0.3), color.rgb(23/256.0,77/256.0,165/256.0)])
c.stroke(path.line(1.4,-2,2,2),[style.linewidth(0.3), color.rgb(23/256.0,77/256.0,165/256.0)])

c.stroke(Liniastart(1.45), [style.linewidth(0.4), color.rgb(23/256.0,77/256.0,165/256.0)])
c.stroke(Liniasrodek(-0.12), [style.linewidth(0.35), color.rgb(23/256.0,77/256.0,165/256.0)])
c.stroke(Liniakoniec(-1.70), [style.linewidth(0.4), color.rgb(23/256.0,77/256.0,165/256.0)])

c.stroke(kolo1, styl1)
c.writePDFfile()




