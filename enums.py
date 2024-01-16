from enum import Enum

class ThrowMotion (Enum):
    Backhand = "backhand"
    Flick = "flick"
    OffHand = "off hand"
    UpsideDown = "upside down"

class ThrowType (Enum):
    Flat = "flat"
    IO = "inside out"
    OI = "outside in"
    High = "high release"
    Hammer = "hammer"
    Scoober = "scoober"
    Blade = "blade"

class ThrowForce (Enum):
    no_mark = "no mark"
    open_throw = "open throw"
    break_throw = "break throw"
    flat_mark = "flat mark"

class PossessionResult (Enum):
    completion = "completion"
    turn = "turn"