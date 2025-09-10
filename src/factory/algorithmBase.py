from abc import ABC
from src.model.classificationResult import ClassificationResult
from src.model.inputData import InputData


class ClassificationAlgorithm(ABC):
    @classmethod
    def classify(self, list) -> ClassificationResult:
     pass

    @classmethod
    def train(self, func):
     pass
