from fastapi import Depends, HTTPException
import time
from src.app.use_cases.DataAnalysisUseCase import DataAnalysisUseCase
from src.presentation.api.schemas.DataAnalysisSchema import (
    DataAnalysisRequest,
    DataAnalysisResponse
)

from src.infra.models.PandasDataFrame import PandasDataFrame

class DataAnalysisController:
    def __init__(self, use_case: DataAnalysisUseCase = Depends(lambda: DataAnalysisUseCase(PandasDataFrame()))):
        self.use_case = use_case

    async def analyze_list(self, request: DataAnalysisRequest) -> DataAnalysisResponse:
        try:
            
            if not request.data:
                raise HTTPException(
                    status_code=400,
                    detail="A lista não pode estar vazia"
                )
            
            analysis = await self.use_case.analyze_data(request.data)
            
            return DataAnalysisResponse(
                analysis_results=analysis.analysis_results,
                total_items=analysis.total_items,
                processing_time=analysis.processing_time
            )
            
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Erro ao analisar lista: {str(e)}"
            )
