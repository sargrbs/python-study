from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class SentimentRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="Texto para análise de sentimento",
        example="Este produto é excelente!"
    )

class SentimentBatchRequest(BaseModel):
    texts: List[str] = Field(
        ...,
        min_items=1,
        max_items=100,
        description="Lista de textos para análise em lote",
        example=[
            "Este produto é excelente!",
            "Não gostei do atendimento",
            "O serviço foi normal"
        ]
    )

class SentimentResponse(BaseModel):
   
    text: str = Field(
        ...,
        description="Texto original analisado"
    )
    sentiment: str = Field(
        ...,
        description="Sentimento identificado (Positivo, Negativo, Neutro)"
    )
    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Nível de confiança da análise"
    )
    created_at: datetime = Field(
        default_factory=datetime.now,
        description="Data e hora da análise"
    )

class SentimentBatchResponse(BaseModel):
    results: List[SentimentResponse] = Field(
        ...,
        description="Lista de resultados das análises"
    )
    total_items: int = Field(
        ...,
        description="Número total de textos analisados"
    )
    processing_time: float = Field(
        ...,
        description="Tempo total de processamento em segundos"
    )
 
class ErrorResponse(BaseModel):
    detail: str = Field(
        ...,
        description="Descrição detalhada do erro"
    )
    error_code: str = Field(
        ...,
        description="Código de identificação do erro"
    )
    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="Data e hora do erro"
    )


class ValidationErrorMessage(BaseModel):
    loc: List[str]
    msg: str
    type: str

class HTTPValidationError(BaseModel):
    detail: List[ValidationErrorMessage]