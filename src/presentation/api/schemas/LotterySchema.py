from pydantic import BaseModel, Field
from typing import List, Dict

class LotteryResponse(BaseModel):
    analysis_results: List[Dict]
    total_items: int
    processing_time: float 

class LotteryAnalyzeResponse(BaseModel):
    analysis_results: List[Dict] 
    total_items: int
    processing_time: float 