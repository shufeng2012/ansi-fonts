'''
Copyright (c) 2026 shufeng2012

ANSI Fonts Package by Python
'''

# Global variables
CLEAR = "\033[0m"

# Froeground colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
CYAN = "\033[36m"

# Background colors
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_PURPLE = "\033[45m"
BG_CYAN = "\033[46m"

# Font styles
BOLD = "\033[1m"        # Bold
DARKEN = "\033[2m"      # Darken
ITALIC = "\033[3m"      # Italic
UDLINE = "\033[4m"      # Underline
SLOW_FLASH = "\033[5m"  # Slow flash  #! Some terminals may not be supported.
FAST_FLASH = "\033[6m"  # Fast flash  #! Some terminals may not be supported.
INVCOLOR = "\033[7m"    # Inverted color
INVISIBLE = "\033[8m"   # Invisible
STKETHROUGH = "\033[9m" # Strikethrough

# Functions
def color(string: str, fg_color: str = CLEAR, bg_color: str = CLEAR, clear: bool = True) -> str:        #! Cannot use both fg_color and bg_color.
    '''
    Provide colorful text function.
    '''

    if (fg_color == CLEAR) and (bg_color == CLEAR):
        return string
    elif (fg_color != CLEAR) and (bg_color != CLEAR):
        print(RED + "ERROR: Cannot use both fg_color and bg_color!" + CLEAR)
        return "Error"
    else:
        if bg_color == CLEAR:
            if clear == True:
                return fg_color + string + CLEAR
            else:
                return fg_color + string
        if fg_color == CLEAR:
            if clear == True:
                return bg_color + string + CLEAR
            else:
                return bg_color + string

def variant(string: str, variant: str = CLEAR, clear: bool = True) -> str:
    '''
    Provide more font styles function.
    '''

    if variant == CLEAR:
        return string
    else :
        re: str = ""
        re += variant + string
        if clear == True:
            re += CLEAR
        return re

def mix(string: str, fg_color: str = CLEAR, bg_color: str = CLEAR, variant: str = CLEAR, clear: bool = True) -> str:    #! Cannot use both fg_color and bg_color.
    '''
    Mix both the two functions.
    '''

    re: str = ""
    if (fg_color == CLEAR) and (bg_color == CLEAR) and (variant == CLEAR):
        return string
    elif (fg_color != CLEAR) and (bg_color != CLEAR) and (variant != CLEAR):
        print(RED + "ERROR: Cannot use both fg_color and bg_color!" + CLEAR)
        return "Error"
    elif variant != CLEAR:
        re += variant
        if (fg_color == CLEAR) and (bg_color == CLEAR):
            re += string
            if clear == True:
                re += CLEAR
        if bg_color == CLEAR:
            if clear == True:
                re += fg_color + string + CLEAR
            else:
                re += fg_color + string
        if fg_color == CLEAR:
            if clear == True:
                re += bg_color + string + CLEAR
            else:
                re += bg_color + string
    else:
        if bg_color == CLEAR:
            if clear == True:
                re += fg_color + string + CLEAR
            else:
                re += fg_color + string
        if fg_color == CLEAR:
            if clear == True:
                re += bg_color + string + CLEAR
            else:
                re += bg_color + string
    return re
