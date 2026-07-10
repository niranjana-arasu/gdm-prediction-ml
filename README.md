# Predicting Gestational Diabetes Mellitus in Pregnant Women: A Visceral Fat Ultrasound Study

Machine learning project predicting Gestational Diabetes Mellitus (GDM) risk using visceral adipose tissue (VAT) ultrasound measurements and clinical data, completed as part of an MSc Data Science dissertation at Coventry University (Distinction).

## Overview

Gestational Diabetes Mellitus affects a significant number of pregnant women and carries risks for both mother and child if detected late. Conventional screening typically identifies GDM in later pregnancy. This project investigates whether **visceral adipose tissue (VAT)**, measured non-invasively via ultrasound, along with other early-pregnancy clinical markers, can support earlier and more accurate GDM risk prediction using machine learning.

## Dataset

- **Source:** [PhysioNet – Visceral adipose tissue measurements during pregnancy](https://doi.org/10.13026/9q68-n048)
- **Size:** 133 women, monitored from early pregnancy through delivery at five hospitals in Porto Alegre, Brazil (Ultrasound Department, Murialdo Teaching Health Centre, Oct 2016–Dec 2017)
- **Features (15):** age, ethnicity, prior diabetes history, blood pressure, VAT measurement (central Armellini fat), gestational age, number of pregnancies, first fasting glucose, pregestational BMI, delivery type, birth weight, and GDM status (target)

## Methodology

**1. Data Preprocessing**
- Imputed missing values (mean/median) for ethnicity, pregnancy count, fasting glucose, and BMI
- Converted gestational age from a "weeks, days" text format into total days for numerical modelling

**2. Exploratory Data Analysis**
- Correlation heatmap to assess relationships between clinical variables and GDM status
- Violin plots and scatter plots to compare feature distributions between GDM-positive and GDM-negative cases

**3. Feature Selection**
- Used Random Forest feature importance to identify the strongest predictors:
  - First fasting glucose
  - BMI (pregestational)
  - Central VAT measurement (Armellini fat)
  - Current gestational age

**4. Class Imbalance Handling**
- Dataset was imbalanced (~87% non-GDM vs. ~13% GDM)
- Applied **SMOTE** (Synthetic Minority Over-sampling Technique) on the training set to generate synthetic minority-class examples

**5. Model Training & Comparison**
Eight classification algorithms were trained and benchmarked:
- Support Vector Machine (SVM)
- Naive Bayes
- Logistic Regression
- K-Nearest Neighbours (KNN)
- Decision Tree
- Random Forest
- Gradient Boosting
- **Perceptron Ensemble (Bagging)**

**6. Evaluation**
- Metrics: Accuracy, Precision, Recall, F1 Score, ROC-AUC
- Validated using 5-fold cross-validation to assess generalizability beyond the single train/test split

## Results

| Classifier | Test Accuracy | Precision | Recall | F1 Score | ROC-AUC | Mean CV Accuracy |
|---|---|---|---|---|---|---|
| SVM | 0.59 | 0.18 | 0.50 | 0.27 | 0.73 | 0.85 |
| Naive Bayes | 0.74 | 0.33 | 0.75 | 0.46 | 0.82 | 0.86 |
| Logistic Regression | 0.78 | 0.38 | 0.75 | 0.50 | 0.85 | 0.87 |
| K-Nearest Neighbour | 0.63 | 0.25 | 0.75 | 0.38 | 0.71 | 0.86 |
| Decision Tree | 0.74 | 0.20 | 0.25 | 0.22 | 0.53 | 0.78 |
| Random Forest | 0.67 | 0.00 | 0.00 | 0.00 | 0.73 | 0.86 |
| Gradient Boosting | 0.67 | 0.14 | 0.25 | 0.18 | 0.73 | 0.83 |
| **Perceptron Ensemble (Bagging)** | **0.78** | **0.40** | **1.00** | **0.57** | **0.85–0.86** | **0.88** |

**Best performing model:** Perceptron Ensemble (Bagging) — achieved the highest cross-validated accuracy (88%) and recall of 100% on the test set, meaning it correctly identified every true GDM case, an important property for a health screening context where false negatives carry the greater clinical risk. Logistic Regression was a close second across most metrics.

Note: Random Forest and Gradient Boosting underperformed on the held-out test set despite generally being strong methods — likely a reflection of the small sample size (133 women, ~18 GDM-positive cases) rather than a flaw in the approach. This is discussed further in the full dissertation.

## Key Takeaways

- VAT ultrasound measurement, combined with fasting glucose, BMI, and gestational age, shows meaningful predictive value for GDM risk
- SMOTE was effective in improving minority-class recall across most models
- Small clinical sample sizes can produce unstable results for complex ensemble methods — cross-validation gave a more reliable picture than the single test split
- Ensemble bagging with simple base learners (Perceptron) outperformed more complex tree-based ensembles on this dataset

## Tech Stack

`Python` `Scikit-learn` `Pandas` `NumPy` `Imbalanced-learn (SMOTE)` `Matplotlib` `Seaborn` `Google Colab`

## Future Work

- Validate on a larger, more diverse cohort to test generalizability
- Explore deep learning approaches for more nuanced GDM subtype classification
- Incorporate longitudinal VAT tracking across pregnancy stages
- Collaborate with clinicians to validate findings for real-world screening use

## Full Report

The complete dissertation, including literature review, full methodology, and ethical approval documentation, is available on request.

## About

This project was completed as part of an MSc in Data Science (Distinction) at Coventry University, 2023–2024.

**Author:** Niranjana Thirunavukkarasu  

**LinkedIn URL:** www.linkedin.com/in/niranjanathirunavukkarasu
