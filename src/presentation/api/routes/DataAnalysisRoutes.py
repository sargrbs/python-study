from fastapi import APIRouter, Depends
from src.presentation.api.controllers.DataAnalysisController import DataAnalysisController
from src.presentation.api.schemas.DataAnalysisSchema import (
    DataAnalysisRequest,
    DataAnalysisResponse,
)
router = APIRouter()

@router.post("/analyze_list", response_model=DataAnalysisResponse)
async def analyze_text(
    request: DataAnalysisRequest,
    controller: DataAnalysisController = Depends()
):
    return await controller.analyze_list(request)
