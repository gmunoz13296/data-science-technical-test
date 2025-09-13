from pydantic import BaseModel
from src.model.classificationResult import ClassificationResult

class OutputResponse(BaseModel):
    results: list[ClassificationResult]
    algorithm: str     