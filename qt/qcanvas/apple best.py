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

    beginknot(174,-79), tensioncurve(), smoothknot(151,-93), tensioncurve(),
    smoothknot(153,-122), tensioncurve(), endknot(170, -139),
])


ogonek = metapost.path.path([
    beginknot(97,-60), tensioncurve(), smoothknot(104,-34), tensioncurve(),
    endknot(130, -20),
    beginknot(130,-20), tensioncurve(), smoothknot(122,-48), tensioncurve(),
    endknot(97, -60)
])

pasek1 = path.path(
    path.moveto(36,-80), path.lineto(51,-61), path.lineto(83,-57), path.lineto(100,-64),
    path.lineto(132,-60), path.lineto(147,-63),path.lineto(158,-68),path.lineto(169,-80),
    path.closepath()
)
pasek2 = path.path(
    path.moveto(36,-80), path.lineto(163,-80), path.lineto(151,-101),
    path.lineto(27,-101), path.closepath()
)
pasek3 = path.rect(30,-101, 122,-22)
pasek4 = path.path(
    path.moveto(28,-122), path.lineto(152,-122), path.lineto(171,-143),
    path.lineto(34,-143), path.closepath()
)
pasek5 = path.path(
    path.moveto(34,-143), path.lineto(171,-143), path.lineto(160,-164),
    path.lineto(45,-164), path.closepath()
)

pasek6 = path.path(
    path.moveto(43,-164), path.lineto(162,-164), path.lineto(138,-186), path.lineto(103,-180),
    path.lineto(72,-186), path.closepath()
)

c.fill(tlo, [deco.filled([color.cmyk.White])])
c.fill(ogonek, [deco.filled([color.rgb.green])])

c.fill(pasek1, [deco.filled([color.rgb.green])])
c.fill(pasek2, [deco.filled([color.cmyk.Goldenrod])])
c.fill(pasek3, [deco.filled([color.cmyk.Peach])])
c.fill(pasek4, [deco.filled([color.cmyk.Red])])
c.fill(pasek5, [deco.filled([color.cmyk.Plum])])
c.fill(pasek6, [deco.filled([color.cmyk.Cyan])])

c.stroke(body, [color.cmyk.White, style.linewidth(8)])

c.writePDFfile('jablko.pdf')