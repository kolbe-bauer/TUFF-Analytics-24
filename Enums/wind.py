from enum import Enum


class WindSpeed(Enum):
    Low = "low"
    Medium = "medium"
    High = "high"


class WindDirection(Enum):
    Upwind = "upwind"
    Downwind = "downwind"
    Right_to_Left = "right to left"
    Left_to_Right = "left to right"
