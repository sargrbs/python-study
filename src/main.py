from fastapi import FastAPI
from src.presentation.api.routes import SentimentRoutes
from src.presentation.api.routes import DataAnalysisRoutes
from src.presentation.api.routes import LotteryRoutes
from src.infra.models.BertModel import BERTSentimentModel
from src.app.use_cases.SentimentAnalysisUseCase import SentimentAnalysisUseCase
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Sentiment Analysis API",
    description="API for sentiment analysis using BERT model",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = BERTSentimentModel()
use_case = SentimentAnalysisUseCase(model=model)

app.include_router(SentimentRoutes.router, prefix="/api")
app.include_router(DataAnalysisRoutes.router, prefix="/api")
app.include_router(LotteryRoutes.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)