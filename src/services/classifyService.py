from src.model.inputData import InputData
from src.factory.algorithmFactory import AlgorithmFactory
from ..model.algorithmType import AlgorithmType
from ..dataset.dataset import DataSet

class ClassifyService():
    
    def classify(self, inputData: InputData):
        factory = AlgorithmFactory()
        algorithm = inputData.algorithm        
        if(not algorithm):
            algorithm = AlgorithmType.LogisticRegression.value
        logistic = factory.create(self.from_string_ci(algorithm))
        return logistic.classify(InputData(numbers=inputData.numbers, algorithm=algorithm))

    def train(self):
        factory = AlgorithmFactory()
        dataset = DataSet()
        services = factory.getAll()
        for service in services:
            service.train(dataset.getDataSet())
        return "successfull"
    
    def from_string_ci(self, value: str):
        if not isinstance(value, str):
            return None
       
        for member in AlgorithmType:
            if member.value.lower() == value.lower():
                return member
        
        return None