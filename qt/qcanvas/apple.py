from pyx import *
from pyx.metapost.path import beginknot, endknot, smoothknot, tensioncurve

c = canvas.canvas()

tlo = path.rect(0,0,200, -210)

body = metapost.path.path([
    beginknot(170,-141), tensioncurve(), smoothknot(154,-171), tensioncurve(),
    smoothknot(129,-185), tensioncurve(), smoothknot(102,-177), tensioncurve(),
    smoothknot(73,-185), tensioncurve(), smoothknot(56,-176), tensioncurve(),
    smoothknot(33,-137), tensioncurve(), smoothknot(29,-115), tensioncurve(),
    smoothknot(29,-100), tensioncurve(), smoothknot(45,-69), tensioncurve(),
    smoothknot(69,-59), tensioncurve(), smoothknot(89,-62), tensioncurve(),
    smoothknot(102,-67), tensioncurve(), smoothknot(130,-59), tensioncurve(),
    smoothknot(150,-62), tensioncurve(), endknot(166,-76),

    beginknot(166,-76), tensioncurve(), smoothknot(149,-93), tensioncurve(),
    smoothknot(151,-122), tensioncurve(), endknot(170, -141),
])

ogonek = metapost.path.path([
    beginknot(97,-60), tensioncurve(), smoothknot(104,-34), tensioncurve(),
    endknot(130, -20),
    beginknot(130,-20), tensioncurve(), smoothknot(122,-48), tensioncurve(),
    endknot(97, -60)
])

pasek1 = path.rect(28,-58, 140,-22)
pasek2 = path.rect(28,-80, 140,-22)
pasek3 = path.rect(28,-101, 140,-22)
pasek4 = path.rect(28,-123, 140,-22)
pasek5 = path.rect(28,-143, 140,-22)
pasek6 = path.rect(28,-164, 140,-22)

c.stroke(tlo, [deco.filled([color.cmyk.White]), color.cmyk.White ])
c.stroke(body, [deco.filled([color.rgb.black]), color.rgb.black ])
c.stroke(ogonek, [deco.filled([color.rgb.green]), color.rgb.green ])

c.stroke(pasek1, [deco.filled([color.rgb.green]), color.rgb.green])
c.stroke(pasek2, [deco.filled([color.cmyk.Goldenrod]), color.cmyk.Goldenrod])

c.writePDFfile('jablko.pdf')
