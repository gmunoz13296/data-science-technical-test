from src.factory.algorithmFactory import AlgorithmFactory
from src.model.algorithmType import AlgorithmType
from src.algorithms.logisticRegressionAlgorithm import LogisticRegressionAlgorithm

class Configure:
    @staticmethod
    def addAlgorithms():
        factory = AlgorithmFactory()
        factory.register(AlgorithmType.LogisticRegression, LogisticRegressionAlgorithm)

