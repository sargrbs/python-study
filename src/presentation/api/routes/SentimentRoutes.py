from fastapi import APIRouter, Depends
from src.presentation.api.controllers.SentimentController import SentimentController
from src.presentation.api.schemas.SentimentSchema import (
    SentimentRequest,
    SentimentBatchRequest,
    SentimentResponse,
    SentimentBatchResponse
)

router = APIRouter()

@router.post("/analyze", response_model=SentimentResponse)
async def analyze_text(
    request: SentimentRequest,
    controller: SentimentController = Depends()
):
    return await controller.analyze_text(request)

@router.post("/analyze/batch", response_model=SentimentBatchResponse)
async def analyze_batch(
    request: SentimentBatchRequest,
    controller: SentimentController = Depends()
):
    return await controller.analyze_batch(request)