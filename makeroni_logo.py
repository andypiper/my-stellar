from time import sleep
from picographics import PicoGraphics, DISPLAY_STELLAR_UNICORN as DISPLAY
from stellar import StellarUnicorn
import jpegdec

MAX_BRIGHT = 0.7
DISPLAY_SECS = 20
INTERVAL_SECS = 10
files = [ "makeroni.jpeg", "hack_wimbledon.jpeg" ]


stellar = StellarUnicorn()
graphics = PicoGraphics(DISPLAY)


def show_image(filename):
    j = jpegdec.JPEG(graphics)
    j.open_file(filename)
    j.decode(0,0,jpegdec.JPEG_SCALE_FULL)
    stellar.set_brightness(MAX_BRIGHT)
    stellar.update(graphics)

def fade_image():
    # poor man's quick fade routine
    for n in range (MAX_BRIGHT*10,-1,-1):
        stellar.set_brightness(n/10)
        stellar.update(graphics)
        sleep(2.5*(n/10))
        if n == 1:
            stellar.clear()


while True:
    for f in files:
        print(f"Show {f}")
        show_image(f)
        sleep(DISPLAY_SECS)
        fade_image()
        sleep(INTERVAL_SECS)
    

# j = jpegdec.JPEG(graphics)
# 
# j.open_file("makeroni.jpeg")
# j.decode(0,0,jpegdec.JPEG_SCALE_FULL)
# 
# stellar.update(graphics)
# 
# sleep(10)




