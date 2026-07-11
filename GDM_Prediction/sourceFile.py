# Load the dataset 
import pandas as pd 
 
# Load the data from the CSV file 
dataset = '/content/visceral_fat.csv' 
data_v = pd.read_csv(dataset) 
 
# Display the first few rows of the dataframe to understand its structure 
data_v.head() 
 
# Inspect the data 
data_v.describe() 
# convert string to numeric 
def convert_to_days(ga_string): 
    """ 
    Convert a gestational age string from 'X weeks, Y days' to total days. 
    """ 
    if isinstance(ga_string, str): 
        parts = ga_string.split(',') 
        if len(parts) == 2: 
            weeks = int(parts[0].strip().split()[0])  # Extracts and converts the weeks part 
            days = int(parts[1].strip().split()[0])   # Extracts and converts the days part 
            return weeks * 7 + days 
    return None 
 
# Apply the conversion function to each column 
data_v['current gestational age'] = data_v['current gestational age'].apply(convert_to_days) 
data_v['gestational age at birth'] = data_v['gestational age at birth'].apply(convert_to_days) 
 
# Display the first few rows of the DataFrame 
data_v.head() 
 
# Correlation matrix 
 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
 
correlation_matrix = data_v.corr() 
plt.figure(figsize=(12, 8)) 
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm') 
plt.title("Correlation Matrix") 
plt.show() 
 
# Handling missing values 
 
# Imputing missing values 
mode_ethnicity = data_v['ethnicity'].mode()[0] 
median_pregnancies = data_v['pregnancies (number)'].median() 
median_glucose = data_v['first fasting glucose (mg/dl)'].median() 
median_bmi = data_v['bmi pregestational (kg/m)'].median() 
 
# Applying the imputations 
data_v['ethnicity'].fillna(mode_ethnicity, inplace=True) 
data_v['pregnancies (number)'].fillna(median_pregnancies, inplace=True) 
data_v['first fasting glucose (mg/dl)'].fillna(median_glucose, 
inplace=True) 
data_v['bmi pregestational (kg/m)'].fillna(median_bmi, inplace=True) 
 
 
imputed_values_summary = data_v.isnull().sum() 
imputed_values_summary 
 
"""EDA 
 
""" 
 
import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
 
# Sample data creation for demonstration 
np.random.seed(0) 
data = pd.DataFrame({ 
    'age (years)': np.random.normal(30, 5, 100), 
    'mean diastolic bp (mmhg)': np.random.normal(70, 10, 100), 
    'mean systolic bp (mmhg)': np.random.normal(120, 15, 100), 
    'central armellini fat (mm)': np.random.normal(25, 5, 100), 
    'current gestational age': np.random.randint(24, 42, 100), 
    'first fasting glucose (mg/dl)': np.random.normal(100, 20, 100), 
    'bmi pregestational (kg/m)': np.random.normal(25, 4, 100), 
    'gestational age at birth': np.random.randint(35, 42, 100), 
    'child birth weight (g)': np.random.normal(3200, 500, 100), 
    'gestational dm': np.random.choice([0, 1], 100) 
}) 
 
# Selecting numerical variables for comparison 
df_num_gdm = data[["age (years)", "mean diastolic bp (mmhg)", 
                 "mean systolic bp (mmhg)", "central armellini fat (mm)", 
                 "current gestational age", "first fasting glucose 
(mg/dl)", 
                 "bmi pregestational (kg/m)", "gestational age at birth", 
                 "child birth weight (g)", "gestational dm"]] 
 
# Creating a different type of visualization for comparison: Violin plots 
fig, ax = plt.subplots(3, 3, figsize=(10, 5))  # Adjusted subplot grid to 
3x3 
for i, column in enumerate(df_num_gdm.columns[:-1]):  # Excluding the last 
'gestational dm' column 
    row = i // 3 
    col = i % 3 
    sns.violinplot(ax=ax[row, col], data=df_num_gdm, y=column, 
x="gestational dm", palette="muted") 
    ax[row, col].set_title(column) 
 
fig.tight_layout() 
plt.show() 
 
import seaborn as sns
# DataFrame with selected columns for pairplot 
df_num_imp = data_v[[ "first fasting glucose (mg/dl)", "bmi pregestational 
(kg/m)", 
"central armellini fat (mm)", "current gestational age", 
"gestational dm"]] 
data_v 
# Generating a pairplot 
sns.pairplot(data=df_num_imp, hue="gestational dm") 
"""FEATURE SELECTION""" 
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split 
# Separate the features and the target 
X = data_v.drop('gestational dm', axis=1) 
y = data_v['gestational dm'] 
# Split the data into training and test sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
random_state=42) 
# Initialize the RandomForestClassifier 
rf = RandomForestClassifier(n_estimators=100, random_state=42) 
# Fit the RandomForestClassifier to the training data 
rf.fit(X_train, y_train) 
# Get feature importances 
importances = rf.feature_importances_ 
# Convert the importances into a DataFrame 
feature_importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': 
importances}) 
# Sort the DataFrame to show the most important features at the top 
feature_importance_df = feature_importance_df.sort_values(by='Importance', 
ascending=False) 
print(feature_importance_df) 
import matplotlib.pyplot as plt 
import numpy as np 
# Get feature importances from the model 
importances = rf.feature_importances_ 
indices = np.argsort(importances)[::-1] 
plt.figure(figsize=(10, 5)) 
plt.title("Feature importances") 
plt.bar(range(X_train.shape[1]), importances[indices], color="r", 
align="center") 
plt.xticks(range(X_train.shape[1]), X_train.columns[indices], rotation=90) 
plt.xlim([-1, X_train.shape[1]]) 
plt.show() 
# Feature selection 
features = ['central armellini fat (mm)', 'bmi pregestational (kg/m)', 
'first fasting glucose (mg/dl)', 'current gestational age'] 
X = data_v[features] 
y = data_v['gestational dm'] 
# Normalization 
from sklearn.preprocessing import MinMaxScaler 
scaler = MinMaxScaler() 
X_scaled = scaler.fit_transform(X) 
# class balancing 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import MinMaxScaler 
from imblearn.over_sampling import SMOTE 
from collections import Counter 
import matplotlib.pyplot as plt 
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, 
test_size=0.2, random_state=42) 
# Apply SMOTE 
smote = SMOTE(random_state=42) 
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train) 
class_distribution_before = Counter(y_train) 
class_distribution_after = Counter(y_train_smote) 
# Plotting class distribution 
fig, axes = plt.subplots(1, 2, figsize=(8, 5), sharey=True) 
axes[0].bar(class_distribution_before.keys(), 
class_distribution_before.values(), color='blue') 
axes[0].set_title('Class Distribution Before SMOTE') 
axes[0].set_xlabel('Class') 
axes[0].set_ylabel('Frequency') 
axes[1].bar(class_distribution_after.keys(), 
class_distribution_after.values(), color='green') 
axes[1].set_title('Class Distribution After SMOTE') 
axes[1].set_xlabel('Class') 
plt.tight_layout() 
plt.show() 
"""MODEL TRAINING""" 
from sklearn.linear_model import LogisticRegression, Perceptron 
from sklearn.naive_bayes import GaussianNB 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.ensemble import RandomForestClassifier, 
GradientBoostingClassifier, BaggingClassifier 
from sklearn.svm import SVC 
from sklearn.metrics import classification_report, accuracy_score, 
precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, 
roc_curve, auc 
import seaborn as sns 
# Define the models 
models = { 
     "SVM": SVC(probability=True), 
    "Logistic Regression": LogisticRegression(), 
    "Naive Bayes": GaussianNB(), 
    "Decision Tree": DecisionTreeClassifier(), 
    "K-Nearest Neighbors": KNeighborsClassifier(), 
    "Random Forest": RandomForestClassifier(), 
    "Gradient Boosting": GradientBoostingClassifier(), 
    "Perceptron Ensemble": BaggingClassifier(base_estimator=Perceptron(), 
n_estimators=10, random_state=42) 
} 
 
# Training, prediction, and evaluation loop 
for name, model in models.items(): 
    # Train the model 
    model.fit(X_train_smote, y_train_smote) 
 
    # Predict on test set 
    y_pred = model.predict(X_test) 
    y_pred_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, 
"predict_proba") else None 
 
    # Performance metrics 
    accuracy = accuracy_score(y_test, y_pred) 
    precision = precision_score(y_test, y_pred) 
    recall = recall_score(y_test, y_pred) 
    f1 = f1_score(y_test, y_pred) 
    roc_auc = roc_auc_score(y_test, y_pred_proba) if y_pred_proba is not 
None else "N/A" 
 
    print(f"Results for {name}:") 
    print(f"Accuracy: {accuracy:.2f}, Precision: {precision:.2f}, Recall: 
{recall:.2f}, F1 Score: {f1:.2f}, ROC-AUC: {roc_auc}") 
 
    # Confusion Matrix 
    conf_matrix = confusion_matrix(y_test, y_pred) 
    plt.figure(figsize=(4, 4)) 
    sns.heatmap(conf_matrix, annot=True, fmt='g') 
    plt.title(f'Confusion Matrix for {name}') 
    plt.ylabel('Actual Label') 
    plt.xlabel('Predicted Label') 
    plt.show() 
 
    # ROC Curve 
    if y_pred_proba is not None: 
        fpr, tpr, _ = roc_curve(y_test, y_pred_proba) 
        roc_auc = auc(fpr, tpr) 
        plt.figure(figsize=(5, 5)) 
        plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve 
(area = {roc_auc:.2f})') 
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--') 
        plt.xlabel('False Positive Rate') 
        plt.ylabel('True Positive Rate') 
        plt.title(f'ROC Curve for {name}') 
        plt.legend(loc="lower right") 
        plt.show() 
 
"""CROSS VALIDATION""" 
 
from sklearn.model_selection import cross_val_score 
from sklearn.linear_model import LogisticRegression, Perceptron 
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.ensemble import RandomForestClassifier, 
GradientBoostingClassifier, BaggingClassifier 
import numpy as np 
 
# Define the models 
models = { 
    "SVM": SVC(probability=True), 
    "Logistic Regression": LogisticRegression(), 
    "Naive Bayes": GaussianNB(), 
    "Decision Tree": DecisionTreeClassifier(), 
    "K-Nearest Neighbors": KNeighborsClassifier(), 
    "Random Forest": RandomForestClassifier(), 
    "Gradient Boosting": GradientBoostingClassifier(), 
    "Perceptron Ensemble": BaggingClassifier(base_estimator=Perceptron(), 
n_estimators=10, random_state=42) 
} 
 
# Perform cross-validation 
cv_scores = {} 
for name, model in models.items(): 
    scores = cross_val_score(model, X_scaled, y, cv=5)  # 5-fold cross
validation 
    cv_scores[name] = scores 
    print(f"Cross-validation scores for {name}: {scores}") 
    print(f"Average score: {np.mean(scores):.2f}") 
 
# Displaying the results 
for model, scores in cv_scores.items(): 
    print(f"{model}: Mean CV Score = {np.mean(scores):.2f}, Standard 
Deviation = {np.std(scores):.2f}") 
 
# Perform cross-validation and store results 
cv_results = {} 
for name, model in models.items(): 
    scores = cross_val_score(model, X_scaled, y, cv=5)  # 5-fold crossvalidation 
    cv_results[name] = np.mean(scores) 
 
# Convert results to a DataFrame for plotting 
cv_df = pd.DataFrame(list(cv_results.items()), columns=['Classifier', 'CV Score']) 
 
# Plotting the results 
plt.figure(figsize=(12, 6)) 
sns.barplot(x='CV Score', y='Classifier', data=cv_df, palette='coolwarm') 
plt.title('Cross-Validation Scores of Different Classifiers') 
plt.xlabel('Average CV Score') 
plt.ylabel('Classifier') 
plt.show()
