from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class DataAnalysis:
    analysis_results: List[dict]
    total_items: int
    processing_time: float
    created_at: datetime = datetime.now()