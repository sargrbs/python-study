from fastapi import Depends, HTTPException
import time

from src.app.use_cases.SentimentAnalysisUseCase import SentimentAnalysisUseCase
from src.presentation.api.schemas.SentimentSchema import (
    SentimentRequest,
    SentimentBatchRequest,
    SentimentResponse,
    SentimentBatchResponse
)
from src.infra.models.BertModel import BERTSentimentModel

class SentimentController:
    def __init__(
        self,
        use_case: SentimentAnalysisUseCase = Depends(lambda: SentimentAnalysisUseCase(BERTSentimentModel()))
    ):
        self.use_case = use_case

    async def analyze_text(self, request: SentimentRequest) -> SentimentResponse:
        try:
            if not request.text.strip():
                raise HTTPException(
                    status_code=400,
                    detail="O texto não pode estar vazio"
                )
            
            analysis = await self.use_case.analyze_text(request.text)
            
            return SentimentResponse(
                text=analysis.text,
                sentiment=analysis.sentiment,
                confidence=analysis.confidence,
                created_at=analysis.created_at
            )
            
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Erro ao analisar texto: {str(e)}"
            )

    async def analyze_batch(self, request: SentimentBatchRequest) -> SentimentBatchResponse:
      
        try:
            start_time = time.time()
            
            if not request.texts:
                raise HTTPException(
                    status_code=400,
                    detail="A lista de textos não pode estar vazia"
                )
            
            if len(request.texts) > 100:
                raise HTTPException(
                    status_code=400,
                    detail="O número máximo de textos por requisição é 100"
                )
            
            analyses = await self.use_case.analyze_batch(request.texts)
            
            processing_time = time.time() - start_time
            
            results = [
                SentimentResponse(
                    text=analysis.text,
                    sentiment=analysis.sentiment,
                    confidence=analysis.confidence,
                    created_at=analysis.created_at
                )
                for analysis in analyses
            ]
            
            return SentimentBatchResponse(
                results=results,
                total_items=len(results),
                processing_time=processing_time
            )
            
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Erro ao analisar textos em lote: {str(e)}"
            )