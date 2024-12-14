from abc import ABC, abstractmethod
from src.domain.entities.DataAnalysis import DataAnalysis
from typing import List

class DataAnalysisModelInterface(ABC):
    @abstractmethod
    def predict(self, data: List[dict]) -> DataAnalysis:
        pass

    @abstractmethod
    def predictLottery(self, data: List[dict]) -> DataAnalysis:
        pass