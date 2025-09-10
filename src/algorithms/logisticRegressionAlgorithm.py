from abc import ABC
from src.factory.algorithmBase import ClassificationAlgorithm
from src.model.classificationResult import ClassificationResult
from ..model.outputResponse import OutputResponse

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

import joblib

class LogisticRegressionAlgorithm(ClassificationAlgorithm):
    def classify(self, inputData) -> ClassificationResult:
     model = joblib.load("model.pkl")
     df_test = pd.DataFrame({'n': inputData.numbers})
     df_test['is3'] = (df_test['n'] % 3 == 0).astype(int)
     df_test['is5'] = (df_test['n'] % 5 == 0).astype(int)
     y_pred = model.predict(df_test[['is3', 'is5']])

     results = [
        ClassificationResult(number=n, predicted_class=cat)
        for n, cat in zip(inputData.numbers, y_pred)
          ]
     return OutputResponse(results=results, algorithm=inputData.algorithm)
     

    def train(self, dataset):
     X_train, X_val, y_train, y_val = dataset
     clf = LogisticRegression(multi_class='multinomial', max_iter=1000, random_state=42)
     clf.fit(X_train, y_train)
     joblib.dump(clf, "model.pkl")  