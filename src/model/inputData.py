from pydantic import BaseModel

class InputData(BaseModel):
    numbers: list[int]
    algorithm: str