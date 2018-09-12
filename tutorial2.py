from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)
mycircle = CircleAsset(5, thinline, blue)
otherCircle=CircleAsset(5, thinline, green)
xcoordinates = range(100, 600, 5)

# Generate a list of sprites that form a line!
spriteBlue = [Sprite(mycircle, (x, x*0.5 + 100)) for x in xcoordinates]
spriteGreen= [Sprite(otherCircle, (x, x*0.25 +100)) for x in xcoordinates]

myapp = App()
myapp.run()
