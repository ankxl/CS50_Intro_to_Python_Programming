import pyfiglet
import sys
import random

def main():
    validate_len_sys_arguments()

def validate_len_sys_arguments():
    if len(sys.argv) == 1 or len(sys.argv) == 3:
        check_contents()
    else:
        sys.exit("Invalid usage")

def check_contents():
    fonts = ["3-d", "3x5", "5lineoblique", "acrobatic", "alligator", "alligator2", "alphabet", "avatar",
             "banner", "banner3-D", "banner3", "banner4", "barbwire", "basic", "bell", "big", "bigchief",
             "binary", "block", "bubble", "bulbhead", "calgphy2", "caligraphy", "catwalk", "chunky",
             "coinstak", "colossal", "computer", "contessa", "contrast", "cosmic", "cosmike", "cricket",
             "cursive", "cyberlarge", "cybermedium", "cybersmall", "diamond", "digital", "doh", "doom",
             "dotmatrix", "drpepper", "eftichess", "eftifont", "eftipiti", "eftirobot", "eftitalic", "eftiwall",
             "eftiwater", "epic", "fender", "fourtops", "fuzzy", "goofy", "gothic", "graffiti", "hollywood",
             "invita", "isometric1", "isometric2", "isometric3", "isometric4", "italic", "ivrit", "jazmine",
             "jerusalem", "katakana", "kban", "larry3d", "lcd", "lean", "letters", "linux", "lockergnome",
             "madrid", "marquee", "maxfour", "mike", "mini", "mirror", "mnemonic", "morse", "moscow",
             "nancyj-fancy", "nancyj-underlined", "nancyj", "nipples", "ntgreek", "o8", "ogre", "pawp",
             "peaks", "pebbles", "pepper", "poison", "puffy", "pyramid", "rectangles", "relief", "relief2",
             "rev", "roman", "rot13", "rounded", "rowancap", "rozzo", "runic", "runyc", "sblood", "script",
             "serifcap", "shadow", "short", "slant", "slide", "slscript", "small", "smisome1", "smkeyboard",
             "smscript", "smshadow", "smslant", "smtengwar", "speed", "stampatello", "standard", "starwars",
             "stellar", "stop", "straight", "tanja", "tengwar", "term", "thick", "thin", "threepoint", "ticks",
             "ticksslant", "tinker-toy", "tombstone", "trek", "tsalagi", "twopoint", "univers", "usaflag", "wavy",
             "weird"]
    if len(sys.argv) == 3:
        if (sys.argv[1] not in ["-f","--font"]):
            sys.exit("Invalid usage")
        elif (sys.argv[2] not in fonts):
            sys.exit("Invalid usage")
        else:
            ch = sys.argv[2]
    else:
        ch = random.choice(fonts)
    string = get_input()
    f = pyfiglet.Figlet(font=ch)
    print(f.renderText(string))

def get_input():
    return(input("Input: "))




main()
