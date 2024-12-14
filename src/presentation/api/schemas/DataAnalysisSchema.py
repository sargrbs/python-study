from pydantic import BaseModel, Field
from typing import List

class DataAnalysisRequest(BaseModel):
    data: List[dict] = Field(..., description="List of data for analysis")
    target_column: str = Field(..., description="Target column for analysis")

class DataAnalysisResponse(BaseModel):
    analysis_results: List[dict] = Field(..., description="Results of data analysis")
    total_items: int = Field(..., description="Total number of items analyzed")
    processing_time: float = Field(..., description="Total processing time in seconds")    