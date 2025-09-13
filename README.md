# data-science-technical-test

## 📌 Project Description
This project solves the **FizzBuzz problem** as a supervised multi-class classification task.  
Instead of using a simple `if/else` approach, we train a machine learning model to classify numbers into one of four classes:

- **None** → numbers not divisible by 3 or 5  
- **Fizz** → numbers divisible by 3 only  
- **Buzz** → numbers divisible by 5 only  
- **FizzBuzz** → numbers divisible by both 3 and 5  

The goal is to demonstrate how a simple problem can be transformed into a complete data science workflow:  
- Dataset creation  
- Model selection and training  
- Model evaluation with test data  
- Cross-validation with multiple algorithms  
- Publishing the trained model as a web service  

---

## 🧠 Theoretical Model & Data Pipeline

### 1️⃣ Data Preparation
We generate a dataset of integers (e.g., from 101 to 5000) and label them using the standard FizzBuzz rules.  
Then, we convert each number into simple **numerical features**:
- `mod_3` → number % 3  
- `mod_5` → number % 5  
- `is3` → 1 if number is divisible by 3, else 0  
- `is5` → 1 if number is divisible by 5, else 0  

This transforms the problem into a linearly separable classification task.

### 2️⃣ Baseline Model: Logistic Regression
We chose **Logistic Regression** as the baseline classifier for the following reasons:

- **Simplicity & Interpretability:** Produces clear, linear decision boundaries, making it easy to understand and explain.  
- **Fast Training:** Very efficient on small datasets, allowing quick iteration.  
- **Probabilistic Outputs:** Provides confidence scores for each class.  
- **Perfect Fit for Problem Structure:** FizzBuzz is fully determined by linear relationships (divisibility), which Logistic Regression can learn perfectly.  

We trained the model using the **One-vs-Rest (OvR)** strategy for multi-class classification and optimized it by minimizing the **cross-entropy loss** function.

### 3️⃣ Model Evaluation
The trained model was tested on numbers **1 to 100** and achieved **100% accuracy** (perfect classification).  
This confirms that the chosen feature set and model are sufficient to solve the problem.

### 4️⃣ Cross-Validation & Model Comparison

We performed **10-fold stratified cross-validation** using the following algorithms:
- Decision Tree  
- Random Forest  
- KNN  
- Support Vector Machine (SVM)  
- Logistic Regression  

**All models achieved 100% accuracy** across all folds.

#### Why Did All Models Perform Perfectly?
This outcome is expected given the nature of the problem and dataset:
- **Perfectly Deterministic Labels:** The FizzBuzz labels are derived from a simple mathematical rule (divisibility by 3 and/or 5). There is no noise or randomness in the data.  
- **Linearly Separable Problem:** The chosen features (`is3`, `is5`) make the classes perfectly separable, meaning that even the simplest models can learn the decision boundaries without error.  
- **Balanced and Sufficiently Large Dataset:** By generating thousands of samples (from 101 to 5000), we ensure that each class (None, Fizz, Buzz, FizzBuzz) is well represented, which prevents overfitting and guarantees that models see enough examples of every case.  
- **Low Complexity of the Task:** The classification task boils down to two binary conditions (divisible by 3, divisible by 5), which can be learned by virtually any supervised algorithm, from linear models to tree-based ensembles.

#### Model Selection After Cross-Validation
Since all models achieved identical performance, we do **not select a single “best” model**.  
Instead, we document that **multiple algorithms are equally capable of solving this problem perfectly**.  

when all candidate models achieve the same result, the final choice can be based on **secondary criteria** such as:
- Training and inference speed  
- Model interpretability  
- Deployment complexity  
- Memory footprint  

For this project, we kept **Logistic Regression** as the baseline model because it is:
- The simplest and most interpretable solution  
- Extremely efficient to train and deploy  
- Sufficient to achieve perfect classification on this task  

---

## How to activate enviroment:
Copy and paste that command into ther terminal:
`.\venv\Scripts\activate`

## How to run:
Copy and paste that command into ther terminal:
`uvicorn main:app --reload`

## How to get test coverage:
Copy and paste that command into ther terminal:
`pytest --cov=. --cov-report=term-missing`

## How to use:
Put in the browser that url: `http://127.0.0.1:8000/docs`, this is the swagger service running.
Now you can use the endpoint: `classifier/classify`, that endpoint accepts the follow param:

`{
  "numbers": [
    0,1
  ],
  "algorithm": ""
}`

The property `numbers` is a list of integers that will be classifiers into the classes:
`FizzBuzz, Fizz, Buzz, None` according the exercise given.
The property `algorithm` is to select the algorithm you can use. For this example the `LogisticRegression` is the only implemented, and if you don't provide any value in that property that algorithm will be use, in other case an error could be throw.
There is an easy way to incorporate a new algorithm.