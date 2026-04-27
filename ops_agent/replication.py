
import datetime
from typing import List, Dict

def compute_trend(history: List[float]) -> str:
    """
    Trend logic:
    - stable: last 3 values difference < 1 sec
    - growing: strictly increasing trend
    - recovering: strictly decreasing trend
    """

    if len(history) < 3:
        return "stable"

    last3 = history[-3:]

    if last3[2] - last3[1] > 0 and last3[1] - last3[0] > 0:
        return "growing"

    if last3[2] - last3[1] < 0 and last3[1] - last3[0] < 0:
        return "recovering"

    return "stable"


def is_degraded(history: List[float]) -> bool:
    if len(history) < 3:
        return False
    return (history[-1] - history[-3]) > 10