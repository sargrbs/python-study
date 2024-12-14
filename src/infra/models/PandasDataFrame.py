from fastapi import Depends, HTTPException
import pandas as pd
from src.app.interfaces.DataAnalysisModelInterface import DataAnalysisModelInterface
from src.domain.entities.DataAnalysis import DataAnalysis
from datetime import datetime
from typing import List

class PandasDataFrame(DataAnalysisModelInterface):
    def predict(self, data: List[dict]) -> DataAnalysis:
        start_time = datetime.now()
        
        df = pd.DataFrame(data)
        
        analysis_results = [
            {
                "total_rows": len(df),
                "numerical_columns": df.select_dtypes(include=['int64', 'float64']).columns.tolist(),
                "summary_stats": df.describe().to_dict(),
                "missing_values": df.isnull().sum().to_dict(),
                "salary_describe": df['salario'].describe().to_dict(),
                "unique_values": {col: df[col].nunique() for col in df.columns}
            }
        ]
        
        end_time = datetime.now()
        processing_time = (end_time - start_time).total_seconds()
        
        return DataAnalysis(
            analysis_results=analysis_results,
            total_items=len(df),
            processing_time=processing_time
        )
    
    def predictLottery(self, data) -> DataAnalysis:
        try:
            df = pd.DataFrame(data)
            
            analysis_results = [{
                "draw_numbers": df["draw_number"].tolist(),
                "balls_frequency": df["balls"].apply(pd.Series).stack().value_counts().to_dict(),
                "total_draws": len(df),
                "summary_stats": {
                    "draws_analyzed": len(df),
                    "unique_numbers": df["balls"].apply(pd.Series).nunique().to_dict()
                }
            }]
            
            return DataAnalysis(
                analysis_results=analysis_results,
                total_items=len(df),
                processing_time=0.0 
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Erro ao analisar resultados da loteria: {str(e)}"
            )