from pynput.mouse import Controller
from pynput.keyboard import Controller

def controlMouse():
    mouse=Controller()
    # left to right 10 pixels top to btm is 20 px
    mouse.position = (500,200)

def controlKeyboard():
    keyboard=Controller()
    keyboard.type("i am awesome!!")

controlKeyboard()

# controlling to your keyboard
# controlling to your mouse
# listening to your mouse