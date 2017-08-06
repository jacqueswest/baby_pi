from subprocess import call

args = ["i2cset", "-y", "1", "0x70"]
whiteLeds = ["0x02", "0x04", "0x05", "0x07"]
irLeds = ["0x01", "0x03", "0x06", "0x08"]
fullBrightness = "0x32"


def all_leds_on():
    call([args[0], args[1], args[2], args[3], "0x00", "0xff"])
    full_gain_all_leds()
    full_bright_all_white_leds()


def all_white_leds_on():
    call([args[0], args[1], args[2], args[3], "0x00", "0x5a"])
    full_gain_all_leds()
    full_bright_all_white_leds()


def all_ir_leds_on():
    call([args[0], args[1], args[2], args[3], "0x00", "0xa5"])
    full_gain_all_leds()
    full_bright_all_ir_leds()


def all_leds_off():
    call([args[0], args[1], args[2], args[3], "0x00", "0x00"])


def full_gain_all_leds():
    call([args[0], args[1], args[2], args[3], "0x09", "0x0f"])


def full_bright_all_white_leds():
    call([args[0], args[1], args[2], args[3], whiteLeds[0], fullBrightness])
    call([args[0], args[1], args[2], args[3], whiteLeds[1], fullBrightness])
    call([args[0], args[1], args[2], args[3], whiteLeds[2], fullBrightness])
    call([args[0], args[1], args[2], args[3], whiteLeds[3], fullBrightness])


def full_bright_all_ir_leds():
    call([args[0], args[1], args[2], args[3], irLeds[0], fullBrightness])
    call([args[0], args[1], args[2], args[3], irLeds[1], fullBrightness])
    call([args[0], args[1], args[2], args[3], irLeds[2], fullBrightness])
    call([args[0], args[1], args[2], args[3], irLeds[3], fullBrightness])


def all_leds_full_brightness():
    full_bright_all_white_leds()
    full_bright_all_ir_leds()


led = {"all": all_leds_on, "white": all_white_leds_on, "ir": all_ir_leds_on, "off": all_leds_off}
