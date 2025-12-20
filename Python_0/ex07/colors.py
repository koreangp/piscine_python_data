USE_COLOR = True

RESET = "\033[0m" if USE_COLOR else ""

BLACK = "\033[30m" if USE_COLOR else ""
RED = "\033[31m" if USE_COLOR else ""
GREEN = "\033[32m" if USE_COLOR else ""
YELLOW = "\033[33m" if USE_COLOR else ""
BLUE = "\033[34m" if USE_COLOR else ""
MAGENTA = "\033[35m" if USE_COLOR else ""
CYAN = "\033[36m" if USE_COLOR else ""
WHITE = "\033[37m" if USE_COLOR else ""


BOLD = "\033[1m" if USE_COLOR else ""
UNDER = "\033[4m" if USE_COLOR else ""

NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}
