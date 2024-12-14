from fastapi import Depends, HTTPException
from datetime import datetime
from src.app.use_cases.DataAnalysisUseCase import DataAnalysisUseCase
from src.app.use_cases.LotteryUseCase import LotteryUseCase
from src.presentation.api.schemas.LotterySchema import (
    LotteryResponse,
    LotteryAnalyzeResponse
)

from src.infra.models.PandasDataFrame import PandasDataFrame
from src.infra.crawler.LotteryCrawler import LotteryCrawler

class LotteryController:
    def __init__(self, 
        use_case: LotteryUseCase = Depends(lambda: LotteryUseCase(LotteryCrawler('https://www.megasena.com/resultados-anteriores'))),
        analysis_use_case: DataAnalysisUseCase = Depends(lambda: DataAnalysisUseCase(PandasDataFrame()))
    ):
        self.use_case = use_case
        self.analysis_use_case = analysis_use_case

    async def lottery_results(self):
        try:
            start_time = datetime.now()
            result = await self.use_case.get_lottery_data()
            processing_time = (datetime.now() - start_time).total_seconds()
            
            return LotteryResponse(
                analysis_results=result,
                total_items=len(result),
                processing_time=processing_time
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Erro ao analisar lista: {str(e)}"
            )
        
    async def analyze_lottery_results(self):
        try:
            start_time = datetime.now()
            result = await self.use_case.get_lottery_data()
            analysis = await self.analysis_use_case.analyze_lottery_data(result)
            processing_time = (datetime.now() - start_time).total_seconds()
            
            return LotteryAnalyzeResponse(
                analysis_results=analysis.analysis_results,
                total_items=len(result),
                processing_time=processing_time
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Erro ao analisar resultado da loteria: {str(e)}"
            )