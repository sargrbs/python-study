from src.domain.entities.Sentiment import SentimentAnalysis
from src.app.interfaces.SentimentModelInterface import SentimentModelInterface
from typing import List

class SentimentAnalysisUseCase:
    def __init__(
        self,
        model: SentimentModelInterface
    ):
        self.model = model

    async def analyze_text(self, text: str) -> SentimentAnalysis:
        analysis = self.model.predict(text)
        return analysis

    async def analyze_batch(self, texts: List[str]) -> List[SentimentAnalysis]:
        analyses = self.model.predict_batch(texts)
        return analyses