class JoyEvent:
    BUTTON_PRESSED  = 0
    BUTTON_RELEASED = 1
    AXIS_MOVED      = 2
    POV_MOVED       = 3
    VECTOR3_MOVED   = 4
    NUM             = 5
    INVALID         = 6

class JoyButtons: # XBox Controller, the buttons need to be checked
    BACK       = 0
    A          = 1
    B          = 2
    X          = 3
    Y          = 4
    LEFT       = 5
    RIGHT      = 6
    START      = 7
    XBOX       = 8
    LEFT_AXIS  = 9
    RIGHT_AXIS = 10
    POV        = 11

    NUM     = 12
    LIST    = [BACK, A, B, X, Y, LEFT, RIGHT, START, XBOX, LEFT_AXIS, RIGHT_AXIS, POV]

class JoyAxes: # XBox Controller
    LEFT_LEFTRIGHT    = 0
    LEFT_UPDOWN       = 1
    LEFT_LEFT         = 2
    RIGHT_LEFTRIGHT   = 3
    RIGHT_UPDOWN      = 4
    RIGHT_RIGHT       = 5
    NUM               = 6

    LIST    = [LEFT_LEFTRIGHT, LEFT_UPDOWN, LEFT_LEFT, RIGHT_LEFTRIGHT, RIGHT_UPDOWN, RIGHT_RIGHT]

