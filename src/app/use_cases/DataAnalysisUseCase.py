from src.domain.entities.DataAnalysis import DataAnalysis
from src.app.interfaces.DataAnalysisModelInterface import DataAnalysisModelInterface
from typing import List

class DataAnalysisUseCase:
    def __init__(
        self,
        model: DataAnalysisModelInterface
    ):
        self.model = model

    async def analyze_data(self, data: List[dict]) -> DataAnalysis:
        return self.model.predict(data)

    async def analyze_lottery_data(self, data) -> DataAnalysis:
        return self.model.predictLottery(data)