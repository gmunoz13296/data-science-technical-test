from pydantic import BaseModel

class ClassificationResult(BaseModel):
    number: int
    predicted_class: str