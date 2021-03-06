class JoyEvent:
    BUTTON_PRESSED = 0
    BUTTON_RELEASED = 1
    AXIS_MOVED = 2
    POV_MOVED = 3
    VECTOR3_MOVED = 4
    NUM = 5
    INVALID = 6


class JoyButtons:  # XBox Controller, the buttons need to be checked
    A = 0
    B = 1
    X = 2
    Y = 3
    LB = 4
    RB = 5
    BACK = 6
    START = 9
    XBOX = 8
    LC = 7
    RC = 10


class JoyAxes:  # XBox Controller
    LEFT_LEFTRIGHT = 0
    LEFT_UPDOWN = 1
    LT = 3
    RIGHT_LEFTRIGHT = 2
    RIGHT_UPDOWN = 5
    RT = 4


