# Predictive Models for Online Shoppers' Purchase Intentions

A comparative study of classification algorithms and ensemble methods for predicting whether an online shopping session will result in a purchase, built on the UCI **Online Shoppers Purchasing Intention** dataset.

## Overview

E-commerce sites generate huge volumes of clickstream data, but only a small fraction of sessions convert into a sale. This project builds and compares classification models that predict purchase intent (`Revenue`: True/False) from session-level browsing behaviour, so that online stores can better identify likely customers and target marketing accordingly.

Four algorithms were trained and evaluated:

- **Naïve Bayes**
- **Logistic Regression**
- **Random Forest** (bagging ensemble)
- **Gradient Boosting Classifier** (boosting ensemble)

## Dataset

- **Source:** [UCI Machine Learning Repository – Online Shoppers Purchasing Intention Dataset](https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset)
- **Size:** 12,330 sessions collected over one year, each representing a unique user
- **Features:** 18 attributes across two groups
  - **Session/pageview data (14):** Administrative, Administrative_Duration, Informational, Informational_Duration, ProductRelated, ProductRelated_Duration, BounceRates, ExitRates, PageValues, SpecialDay, OperatingSystems, Browser, Region, TrafficType
  - **Real-world context (4):** Month, VisitorType, Weekend, Revenue (target)
- **Class imbalance:** 84.5% negative (no purchase) vs. 15.5% positive (purchase) — 10,422 negative / 1,908 positive sessions

## Methodology

1. **Data Cleaning** — handled missing values, duplicates, and encoded categorical fields (e.g. month name → numeric, visitor type → numeric).
2. **Exploratory Analysis** — histograms to inspect distributions/outliers; a correlation heatmap to detect redundant features (e.g. `Administrative` vs `Administrative_Duration`, `BounceRates` vs `ExitRates`).
3. **Class Balancing** — addressed the 84.5/15.5 imbalance using **SMOTE** (synthetic oversampling of the minority/purchase class) and **random undersampling**, applied only to the training set.
4. **Feature Encoding** — one-hot encoding of categorical variables (58 input features after encoding), chosen over label encoding to avoid introducing artificial ordinality.
5. **Modelling** — 70/30 train-test split; each algorithm trained on the raw, oversampled, and undersampled data for a fair comparison.
6. **Evaluation** — Accuracy, Precision, Recall, F1-score, and AUC via cross-validation and confusion matrices.
7. **Hyperparameter Tuning** — `GridSearchCV` applied to the best-performing model (Gradient Boosting) via a `sklearn` Pipeline.

## Results

| Classifier | Accuracy | F1 Score | Precision | Recall | AUC |
|---|---|---|---|---|---|
| **Gradient Boosting** | **0.906** | **0.662** | 0.694 | 0.633 | **0.941** |
| Random Forest | 0.899 | 0.640 | 0.667 | 0.561 | 0.852 |
| Logistic Regression | 0.889 | 0.493 | **0.730** | 0.372 | 0.890 |
| Naïve Bayes | 0.856 | 0.531 | 0.503 | 0.561 | 0.852 |

**Gradient Boosting** was the top-performing model overall, and after `GridSearchCV` hyperparameter tuning (`max_depth=5`, `max_leaf_nodes=5`, `min_samples_leaf=5`) achieved a mean accuracy of **90.7%**.

## Tech Stack

- **Language:** Python
- **Libraries:** `scikit-learn`, `pandas`, `numpy`, `imbalanced-learn` (SMOTE), `matplotlib`, `seaborn`

## Repository Structure

```
├── data/                     # Dataset (online_shoppers_intention.csv)
├── notebooks/                # Jupyter notebooks for EDA, preprocessing, modelling
├── README.md
└── requirements.txt
```

*(Adjust the structure above to match your actual repo layout.)*

## Key Takeaways

- Ensemble methods (Gradient Boosting, Random Forest) outperformed single classifiers on this dataset.
- Highly correlated feature pairs (e.g. duration vs. count features) were identified and considered for removal to reduce redundancy.
- Class balancing via SMOTE was essential given the ~85/15 class split, to avoid a model biased toward predicting "no purchase."
- Hyperparameter tuning combined with `GridSearchCV` improved both accuracy and training efficiency.


## About

This project was completed as part of an MSc in Data Science (Distinction) at Coventry University, 2023–2024.

**Author:** Niranjana Thirunavukkarasu
**LinkedIn:** www.linkedin.com/in/niranjanathirunavukkarasu