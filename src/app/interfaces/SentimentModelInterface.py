from abc import ABC, abstractmethod
from src.domain.entities.Sentiment import SentimentAnalysis
from typing import List

class SentimentModelInterface(ABC):
    @abstractmethod
    def predict(self, text: str) -> SentimentAnalysis:
        pass

    @abstractmethod
    def predict_batch(self, texts: List[str]) -> List[SentimentAnalysis]:
        pass