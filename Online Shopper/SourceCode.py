import calendar
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import confusion_matrix, roc_curve, auc, roc_auc_score, accuracy_score, precision_score, recall_score, f1_score
import warnings

warnings.filterwarnings('ignore')

# Load train data
data_os = pd.read_csv('online_shoppers_intention.csv')
print(data_os.describe())

# Exploring and cleaning the data
visitor_type_mapping = {'New_Visitor': 0, 'Returning_Visitor': 1, 'Other': 2}
d_shop = data_os.replace({'VisitorType': visitor_type_mapping})

# Convert month column to numeric values
month_mapping = {v: i for i, v in enumerate(calendar.month_abbr)}
d_shop['Month'] = d_shop['Month'].map(month_mapping)

# Delete records with NAs
d_shop.dropna(inplace=True)
print(d_shop.head())
# Separate features and target variable
X = d_shop.drop("Revenue", axis=1)
y = d_shop['Revenue']

# Encode categorical features
categorical_features = X.select_dtypes(include=['object']).columns.tolist()
X_encoded = pd.get_dummies(X[categorical_features])
X = pd.concat([X.drop(categorical_features, axis=1), X_encoded], axis=1)

# Apply SMOTE oversampling
smote = SMOTE()
X_resampled, y_resampled = smote.fit_resample(X, y)

# Plotting the original class distribution
plt.figure(figsize=(5, 5))
revenue_counts = data_os['Revenue'].value_counts()
labels = revenue_counts.index
sizes = revenue_counts.values
explode = (0.1, 0)
colors = ['tomato', 'cornflowerblue']
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 15})
plt.title('Revenue', fontsize=15)
plt.axis('equal')
plt.show()

# Plotting the balanced class distribution
plt.figure(figsize=(5, 5))
balanced_counts = y_resampled.value_counts()
labels = balanced_counts.index
sizes = balanced_counts.values
colors = ['tomato', 'cornflowerblue']
explode = (0.1, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 15})
plt.title('Revenue (Balanced)', fontsize=18)
plt.axis('equal')
plt.ylabel('')
plt.show()
# Drop the 'Revenue' column from the DataFrame for analysis
df_without_revenue = d_shop.drop("Revenue", axis=1)

# Create the histograms
fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(10, 10))
plt.tight_layout()
df_without_revenue.hist(ax=axes, bins=10)
plt.suptitle('Histogram for input variables', y=1.03, fontsize=16)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Feature Correlation Heatmap
plt.figure(figsize=(10, 6))
correlation_matrix = d_shop.corr()
sns.heatmap(correlation_matrix, cmap="Reds", annot=True)
plt.title('Correlation Heatmap', fontsize=18)
plt.show()

# Scatter plots to examine relationship with target
plt.figure(figsize=(12, 6))
features_to_plot = ['BounceRates', 'ProductRelated', 'Administrative', 'Informational']
titles = ['Bounce Rate', 'Product Related', 'Administrative', 'Informational']

for i, feature in enumerate(features_to_plot):
    plt.subplot(2, 2, i + 1)
    sns.scatterplot(x=feature, y='Revenue', data=d_shop, hue="Revenue")
    plt.title(titles[i], fontweight='bold', fontsize=15)

plt.tight_layout()
plt.show()
# Split the dataset into features and target variable after selection
selected_features = ['Administrative', 'Informational', 'ProductRelated', 'BounceRates', 'PageValues', 'Month', 'Region', 'TrafficType', 'VisitorType']
X = d_shop[selected_features]
y = d_shop["Revenue"]

# Convert remaining categorical features into numeric using one-hot encoding
X = pd.get_dummies(X)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize classifiers
classifiers = {
    "Random Forest": RandomForestClassifier(),
    "Naive Bayes": GaussianNB(),
    "Gradient Boosting": GradientBoostingClassifier(),
    "Sub-Logistic Regression": LogisticRegression()
}

results = []

# Evaluate each classifier
for name, clf in classifiers.items():
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    
    y_pred_prob = clf.predict_proba(X_test)[:, 1]
    auc_score = roc_auc_score(y_test, y_pred_prob)
    
    results.append({
        "Classifier": name,
        "Accuracy": accuracy,
        "F1 Score": f1,
        "Precision": precision,
        "Recall": recall,
        "AUC": auc_score
    })

df_results = pd.DataFrame(results)
print("Results:")
print(df_results)

# Plot Evaluation Metrics
metrics = ["Accuracy", "F1 Score", "Precision", "Recall", "AUC"]
bar_width = 0.15
x_pos = np.arange(len(df_results))

plt.figure(figsize=(10, 5))
for i, metric in enumerate(metrics):
    plt.bar(x_pos + (i * bar_width), df_results[metric], width=bar_width, label=metric)

plt.xlabel("Classifier")
plt.ylabel("Scores")
plt.title("Evaluation Metrics of Classifiers")
plt.ylim([0, 1])
plt.xticks(x_pos + bar_width * 2, df_results["Classifier"], rotation=45)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()

# Generate Confusion Matrices
for name, clf in classifiers.items():
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    
    plt.figure(figsize=(5, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title(f"Confusion Matrix - {name}")
    plt.ylabel("Actual")
    plt.xlabel("Predicted")
    plt.show()
# Creating the pipelines
pipeline_lr = Pipeline([('lr_classifier', LogisticRegression(random_state=0))])
pipeline_randomforest = Pipeline([('rf_classifier', RandomForestClassifier())])
pipeline_nb = Pipeline([('nb_classifier', GaussianNB())])
pipeline_gb = Pipeline([('gb_classifier', GradientBoostingClassifier())])

pipelines = [pipeline_lr, pipeline_randomforest, pipeline_nb, pipeline_gb]
pipe_dict = {0: 'Logistic Regression', 1: 'RandomForest', 2: 'Naive Bayes', 3: 'Gradient Boosting Classifier'}

best_accuracy = 0.0
best_classifier = None

# Fit pipelines and calculate cross-validation scores
for i, model in enumerate(pipelines):
    model.fit(X_train, y_train)
    scores = cross_val_score(model, X_train, y_train, cv=5)
    mean_accuracy = scores.mean()
    print("{} Mean Accuracy: {:.2f}%".format(pipe_dict[i], mean_accuracy * 100))

# Choosing the best model on test data
for i, model in enumerate(pipelines):
    if model.score(X_test, y_test) > best_accuracy:
        best_accuracy = model.score(X_test, y_test)
        best_classifier = i

print('Classifier with best accuracy: {}'.format(pipe_dict[best_classifier]))
# Create a tuning pipeline
pipe = make_pipeline(GradientBoostingClassifier())

# Define grid parameters
grid_param = [
    {
        "gradientboostingclassifier": [GradientBoostingClassifier()],
        "gradientboostingclassifier__n_estimators":
        "gradientboostingclassifier__max_depth": [5, 8, None],
        "gradientboostingclassifier__min_samples_leaf":,
        "gradientboostingclassifier__max_leaf_nodes": [2, 5]
    }
]

# Grid search configuration
gridsearch = GridSearchCV(pipe, grid_param, cv=2, verbose=0, n_jobs=-1)
best_model = gridsearch.fit(X_train, y_train)

print("Best Model:", best_model.best_estimator_)
print("The mean accuracy of the model is: {:.2f}%".format(best_model.score(X_test, y_test) * 100))
