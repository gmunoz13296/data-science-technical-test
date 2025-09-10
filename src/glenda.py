# =======================================
# FizzBuzz as a Supervised Classification Problem
# =======================================
# Objective: Predict Fizz/Buzz/FizzBuzz/None for numbers 1 to 100
# using a supervised learning model trained on synthetic data.
# =======================================

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# --------------------------
# FizzBuzz Labeling Function
# --------------------------
def fizzbuzz_label(n):
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

# -----------------------------
# Training Dataset Construction
# -----------------------------
# Train on numbers 101..5000 to avoid overlap with test set 1..100
df_train = pd.DataFrame({'n': np.arange(101, 5001)})

# Binary features
df_train['is3'] = (df_train['n'] % 3 == 0).astype(int)
df_train['is5'] = (df_train['n'] % 5 == 0).astype(int)

# Target labels
df_train['label'] = df_train['n'].map(fizzbuzz_label)

# Features and target
X = df_train[['is3', 'is5']]
y = df_train['label']

# --------------------------
# Optional internal hold-out (stratified)
# --------------------------
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# --------------------------
# Base Model Training
# --------------------------
clf = LogisticRegression(multi_class='multinomial', max_iter=1000, random_state=42)
clf.fit(X_train, y_train)

# --------------------------
# Test: Numbers 1 to 100
# --------------------------
df_test = pd.DataFrame({'n': np.arange(1, 101)})
df_test['is3'] = (df_test['n'] % 3 == 0).astype(int)
df_test['is5'] = (df_test['n'] % 5 == 0).astype(int)
y_test = df_test['n'].map(fizzbuzz_label)

# Predictions
y_pred = clf.predict(df_test[['is3', 'is5']])

# Accuracy and classification report
print("✅ Accuracy on [1..100]:", accuracy_score(y_test, y_pred))
print("\nClassification report:\n", classification_report(y_test, y_pred, digits=4))

# Print results 1..100
print("\n--- FizzBuzz Predictions 1..100 ---")
for n, label in zip(df_test['n'], y_pred):
    print(f"{n}: {label}")

# --------------------------
# 10-Fold Stratified CV and Model Comparison
# --------------------------
models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Logistic Regression": LogisticRegression(max_iter=1000, multi_class='multinomial', random_state=42),
    "SVM": SVC(kernel="rbf", gamma="scale", probability=False)
}

print("\n🔎 10-Fold Stratified Cross-Validation Results:")
results = {}
skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)

for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=skf, scoring="accuracy", n_jobs=-1)
    results[name] = (scores.mean(), scores.std())
    print(f"{name}: mean={scores.mean():.4f} ± {scores.std():.4f}")

# --------------------------
# Select all best models in case of tie
# --------------------------
max_mean = max([v[0] for v in results.values()])  # find highest mean accuracy
best_models = [name for name, (mean, std) in results.items() if mean == max_mean]

print(f"\n👉 Best model(s) (CV) with mean accuracy = {max_mean:.4f}: {', '.join(best_models)}")

# --------------------------
# Retrain all best models on full training set and evaluate on test 1..100
# --------------------------
for best_model_name in best_models:
    final_model = models[best_model_name].fit(X, y)
    final_pred = final_model.predict(df_test[['is3', 'is5']])
    print(f"\n✅ Final test accuracy for {best_model_name} on [1..100]: {accuracy_score(y_test, final_pred)}")