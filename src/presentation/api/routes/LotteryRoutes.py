from fastapi import APIRouter, Depends
from src.presentation.api.controllers.LotteryController import (
    LotteryController,
)
from src.presentation.api.schemas.LotterySchema import (
    LotteryResponse,
)
router = APIRouter()

@router.get("/lottery_results", response_model=LotteryResponse)
async def get_lottery_results(
    controller: LotteryController = Depends()
):
    return await controller.lottery_results()

@router.get("/analyze_lottery_results", response_model=LotteryResponse)
async def get_lottery_results(
    controller: LotteryController = Depends()
):
    return await controller.analyze_lottery_results()
