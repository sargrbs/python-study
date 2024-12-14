from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class SentimentAnalysis:
    text: str
    sentiment: str
    confidence: float
    created_at: datetime = datetime.now()