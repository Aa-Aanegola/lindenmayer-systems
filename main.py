from lSystem import *

axiom = '-YF'

ruleX = [Rule('XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-', 1.0)]
ruleY = [Rule('+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY', 1.0)]
ruleset = {'X':ruleX, 'Y':ruleY}
ls = Lsystem(axiom , ruleset)

ls.generate(4)
ls.set_turtle({"heading": 90, "position": (540, -540)})
ls.draw(angle=90, dist=20, fast=True)
