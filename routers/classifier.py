from fastapi import APIRouter
from pydantic import BaseModel
from src.model.inputData import InputData
from src.model.outputResponse import OutputResponse
from src.services.classifyService import ClassifyService
from src.factory.configure import Configure

router = APIRouter(prefix="/classifier", tags=["classifier"])
Configure.addAlgorithms()

service = ClassifyService()

@router.post("/classify", response_model=OutputResponse)
def classifyNumbers(inputData: InputData):    
    return service.classify(inputData)
