from enum import Enum


class ThrowType(Enum):
    Backhand = "backhand"
    Flick = "flick"
    Off_Hand = "off hand"
    UpsideDown = "upside down"


class ThrowSubtype(Enum):
    Flat = "flat"
    IO = "inside out"
    OI = "outside in"
    High_Release = "high release"
    Hammer = "hammer"
    Scoober = "scoober"
    Blade = "blade"


class ThrowForce(Enum):
    No_Mark = "no mark"
    Force_side_Throw = "open throw"
    Break_side_Throw = "break throw"
    Flat_Mark = "flat mark"


class ThrowOutcome(Enum):
    Catch = 'catch'
    Drop = 'drop'
    Turnover = 'turnover'
    Goal = 'goal'


class ThrowDecision(Enum):
    Good = "good"
    Bad = "bad"


class ThrowAspirations(Enum):
    Reset = "reset"
    Stagnant_Downfield = "stagnant downfield"
    Downfield_Continuation = "downfield continuation"
    Swing_Continuation = "swing continuation"
    Bail_Out = "bail out"
    Centering_Pass = "centering pass"
    Dish = "dish"


class ComingOutOfTimeout(Enum):
    Yes = "yes"
    No = "no"
