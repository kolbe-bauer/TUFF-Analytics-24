from enum import Enum

class ThrowType (Enum):
    Backhand = "backhand"
    Flick = "flick"
    OffHand = "off hand"
    UpsideDown = "upside down"

class ThrowSubtype (Enum):
    Flat = "flat"
    IO = "inside out"
    OI = "outside in"
    High = "high release"
    Hammer = "hammer"
    Scoober = "scoober"
    Blade = "blade"

class ThrowForce (Enum):
    No_Mark = "no mark"
    Open_Throw = "open throw"
    Break_Throw = "break throw"
    Flat_Mark = "flat mark"

class ThrowOutcome (Enum):
    Catch = 'catch'
    Drop = 'drop'
    Turnover = 'turnover'
    Goal = 'goal'

class ThrowDecision (Enum):
    Good = "good"
    Bad = "bad"