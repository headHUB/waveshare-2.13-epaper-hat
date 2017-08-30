#!/usr/bin/env python
# -*- coding: utf-8 -*-
#############################
#
# This converts *some* images into a format that can then be displayed on a waveshare screen.
# Some images it doesnt convert and crashes out, not sure why. 
# code is based off: https://gist.github.com/Akkiesoft/af7470d6f4efec1ddf92d9b531646009 
# code to upoad to a screen is here: https://gist.github.com/Akkiesoft/f3ba94af42138a3756bac426982f57d9
# would prefer to replace this with an ImageMagick line, but no luck yet.
# images generated with ImageMagick seem to display nicely, thats about it 
#
#############################
import os
import sys
import json
from StringIO import StringIO
from PIL import Image,ImageDraw,ImageFont,ImageOps      #http://pillow.readthedocs.io/en/3.4.x/reference/Image.html
import textwrap

palette = [         #this is the colour pallet as needed by the screen. 
    255, 255, 255,
    0, 0, 0,
]

size = 250, 122   #set the size variable, found via the webpage for the lib 
im = Image.open("in.png")      #open a file in the same dir, figure this will be easier for the mo?
if im.mode == 'RGBA':                   #checks to see if its .. RGBA?
    r,g,b,a = im.split()                  #ducks with the colour? 
    im = Image.merge('RGB', (r,g,b))      #not sure..
im.thumbnail(size)                      #changes it to the size defined above
im = ImageOps.invert(im)              #inverts it? 
im.putpalette(palette)              #applies the palette, most of the time, or sometimes it crashes, fun like that 
im.save('image.png')      #saves it 
