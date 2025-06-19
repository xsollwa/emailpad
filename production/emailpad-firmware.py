# This is a hackpad for making email writing faster!

# Import all the IOs of the board
import board

# Imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler


# Main instance of the keyboard
keyboard = KMKKeyboard()

# Adding the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Adding the encoder
encoder=EncoderHandler()
keyboard.modules.append(encoder)

# Defining pins 
PINS = [board.GP27, board.GP28, board.GP29]
encoder.pins=((board.GP0, board.GP1),)

# Telling kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Defining buttons
keyboard.keymap = [
    [
     KC.MACRO("I hope this email finds you well."), 
     KC.MACRO("Best wishes,\nRuzanna"), 
     KC.MACRO("Please let me know if you have any questions"), 
    ]
]

# Encoder sends tab when turned right, and sends shift tab when turned left
encoder.map=[
    (KC.LSFT(KC.TAB), KC.TAB)
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
