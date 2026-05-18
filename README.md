# gdm-prediction-ml
# Predicting Gestational Diabetes Mellitus (GDM) Using Machine Learning

## Project Overview

Gestational Diabetes Mellitus (GDM) affects approximately 14% of pregnancies worldwide and poses serious health risks to both mother and child if undetected. Early, accurate prediction is critical for timely clinical intervention.

This project builds and compares multiple supervised machine learning classifiers to predict GDM risk in pregnant women, using visceral adipose tissue (VAT) measurements and related clinical features derived from a publicly available dataset.

---

## Problem Statement

Can machine learning models reliably identify GDM risk earlier and more accurately than traditional clinical screening methods, using non-invasive measurement data?

---

## Dataset

- **Source:** Publicly available dataset (Kaggle / UCI repository)
- **Features include:** VAT measurements, age, BMI, blood glucose levels, insulin levels, and other clinical indicators
- **Target variable:** GDM diagnosis (binary: positive / negative)

---

## Methodology

1. **Exploratory Data Analysis (EDA)** — distribution analysis, missing value treatment, correlation heatmaps
2. **Data Preprocessing** — feature scaling, handling class imbalance, train/test split (80/20)
3. **Model Training & Comparison** — three classifiers trained and evaluated:
   - Logistic Regression (baseline)
   - Random Forest Classifier
   - Support Vector Machine (SVM)
4. **Evaluation Metrics** — Accuracy, Precision, Recall, F1-Score, ROC-AUC

---

## Results

| Model | Accuracy | Notes |
|---|---|---|
| Logistic Regression | Baseline | Used as interpretable reference model |
| Support Vector Machine | — | Evaluated across kernel types |
| **Random Forest** | **>80%** | **Best performing model** |

Random Forest achieved the highest predictive accuracy, demonstrating the value of ensemble methods for clinical risk classification tasks.

---

## Technologies Used

- **Language:** Python 3
- **Libraries:** pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn
- **Environment:** Jupyter Notebook

---

## Key Findings

- VAT measurements were among the strongest predictors of GDM risk
- Random Forest outperformed Logistic Regression and SVM on both accuracy and F1-score
- Class imbalance handling significantly improved recall for positive GDM cases — critical in a clinical context where false negatives carry high risk

---

## About

This project was completed as part of an MSc in Data Science (Distinction) at Coventry University, 2023–2024.

**Author:** Niranjana Thirunavukkarasu  

**LinkedIn URL:** www.linkedin.com/in/niranjanathirunavukkarasu
