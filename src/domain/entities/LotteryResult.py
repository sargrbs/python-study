from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class LotteryResult:
    draw_number: int
    balls: List
    prize: str
    result: str
    date: datetime