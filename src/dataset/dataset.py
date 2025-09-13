import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score

class DataSet():

    def fizzbuzz_label(self, n):
        """
        Returns the Fizz/Buzz/FizzBuzz/None label for a given number
        according to the classic FizzBuzz rules.
        """
        if n % 3 == 0 and n % 5 == 0:
            return "FizzBuzz"
        elif n % 3 == 0:
            return "Fizz"
        elif n % 5 == 0:
            return "Buzz"
        else:
            return "None"
        
    def getDataSet(self):
        # -----------------------------
        # Training Dataset Construction
        # -----------------------------
        # Train on numbers 101..5000 to avoid overlap with test set 1..100
        df_train = pd.DataFrame({'n': np.arange(101, 5001)})

        # Binary features
        df_train['is3'] = (df_train['n'] % 3 == 0).astype(int)
        df_train['is5'] = (df_train['n'] % 5 == 0).astype(int)

        # Target labels
        df_train['label'] = df_train['n'].map(self.fizzbuzz_label)

        # Features and target
        X = df_train[['is3', 'is5']]
        y = df_train['label']

        # --------------------------
        # Optional internal hold-out (stratified)
        # --------------------------
        return train_test_split(
            X, y, test_size=0.2, stratify=y, random_state=42
        )
